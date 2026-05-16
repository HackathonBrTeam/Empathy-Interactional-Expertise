import re

from empathy_engine.i18n.locales.en import (
    OUTPUT_TRANSLATIONS as EN_OUTPUT_TRANSLATIONS,
)
from empathy_engine.i18n.locales.en import UI_TRANSLATIONS as EN_UI_TRANSLATIONS
from empathy_engine.i18n.locales.es import (
    OUTPUT_TRANSLATIONS as ES_OUTPUT_TRANSLATIONS,
)
from empathy_engine.i18n.locales.es import UI_TRANSLATIONS as ES_UI_TRANSLATIONS
from empathy_engine.i18n.locales.pt_br import (
    OUTPUT_TRANSLATIONS as PT_BR_OUTPUT_TRANSLATIONS,
)
from empathy_engine.i18n.locales.pt_br import UI_TRANSLATIONS as PT_BR_UI_TRANSLATIONS


PROCESSING_LANGUAGE = "en"
SUPPORTED_UI_LANGUAGES = ("en", "pt-BR", "es")
AUTO_LANGUAGE_VALUES = {"auto", "detect", "detected", "user", "user_language"}


LANGUAGE_LABELS = {
    "en": "English",
    "pt-BR": "Português (Brasil)",
    "es": "Español",
}


OUTPUT_LANGUAGE_NAMES = {
    "en": "English",
    "pt-BR": "Brazilian Portuguese",
    "es": "Spanish",
}


TRANSLATIONS = {
    "en": EN_UI_TRANSLATIONS,
    "pt-BR": PT_BR_UI_TRANSLATIONS,
    "es": ES_UI_TRANSLATIONS,
}


OUTPUT_TRANSLATIONS = {
    "en": EN_OUTPUT_TRANSLATIONS,
    "pt-BR": PT_BR_OUTPUT_TRANSLATIONS,
    "es": ES_OUTPUT_TRANSLATIONS,
}


LANGUAGE_HINTS = {
    "pt-BR": (
        " que ", " nao ", " não ", " uma ", " meu ", " minha ", " colega ",
        " reuniao ", " reunião ", " porque ", " estava ", " voce ", " você ",
        " achei ", " achou ", " mensagem ", " obrigado ", " obrigada ",
        " intenção ", " pergunte ", " ajudaria ", " ambas ",
    ),
    "es": (
        " que ", " no ", " una ", " mi ", " colega ", " reunion ", " reunión ",
        " porque ", " estaba ", " usted ", " mensaje ", " gracias ", " penso ",
        " pensó ", " persona ", " la ", " intención ", " pregunta ", " ayudaría ",
        " ambas ",
    ),
    "en": (
        " the ", " and ", " my ", " coworker ", " meeting ", " because ",
        " was ", " were ", " thought ", " message ", " rude ", " clear ",
    ),
}


def normalize_language(language: str | None) -> str:
    if not language:
        return "en"

    lowered = language.strip().lower()

    if lowered in {"pt", "pt-br", "pt_br", "portuguese", "portugues"}:
        return "pt-BR"
    if lowered in {"es", "es-es", "es_mx", "spanish", "espanol"}:
        return "es"
    if lowered in {"en", "en-us", "en-gb", "english"}:
        return "en"

    return "en"


def detect_language_from_locale(locale: str | None) -> str | None:
    if not locale or not locale.strip():
        return None

    normalized = locale.strip().lower().replace("_", "-")

    if normalized.startswith("pt"):
        return "pt-BR"
    if normalized.startswith("es"):
        return "es"
    if normalized.startswith("en"):
        return "en"

    return None


def detect_language_from_accept_language(header: str | None) -> str | None:
    if not header or not header.strip():
        return None

    for option in header.split(","):
        language_tag = option.split(";")[0].strip()
        detected = detect_language_from_locale(language_tag)
        if detected:
            return detected

    return None


def detect_language_from_timezone(timezone: str | None) -> str | None:
    if not timezone or not timezone.strip():
        return None

    normalized = timezone.strip().lower()

    brazil_timezones = {
        "america/araguaina",
        "america/bahia",
        "america/belem",
        "america/boa_vista",
        "america/campo_grande",
        "america/cuiaba",
        "america/fortaleza",
        "america/maceio",
        "america/manaus",
        "america/noronha",
        "america/porto_velho",
        "america/recife",
        "america/rio_branco",
        "america/santarem",
        "america/sao_paulo",
    }

    spanish_timezones = (
        "america/argentina/",
        "america/bogota",
        "america/caracas",
        "america/guatemala",
        "america/lima",
        "america/mexico_city",
        "america/montevideo",
        "america/santiago",
        "europe/madrid",
    )

    if normalized in brazil_timezones:
        return "pt-BR"
    if normalized in {"europe/london", "america/new_york", "america/chicago"}:
        return "en"
    if any(normalized.startswith(prefix) for prefix in spanish_timezones):
        return "es"

    return None


def should_auto_detect_language(language: str | None) -> bool:
    if language is None:
        return True
    return language.strip().lower() in AUTO_LANGUAGE_VALUES


def get_default_ui_language() -> str:
    from empathy_engine.config import load_settings

    return load_settings().default_ui_language


def get_processing_language() -> str:
    from empathy_engine.config import load_settings

    return load_settings().processing_language


def translate(language: str, key: str):
    normalized = normalize_language(language)
    return TRANSLATIONS.get(normalized, EN_UI_TRANSLATIONS).get(
        key,
        EN_UI_TRANSLATIONS.get(key, key),
    )


def validate_translation_coverage() -> dict[str, set[str]]:
    required_keys = set(EN_UI_TRANSLATIONS)
    return {
        language: required_keys - set(translations)
        for language, translations in TRANSLATIONS.items()
        if required_keys - set(translations)
    }


def output_language_name(language: str | None) -> str:
    return OUTPUT_LANGUAGE_NAMES[normalize_language(language)]


def translate_output_text(text: str, language: str | None) -> str:
    normalized = normalize_language(language)
    if normalized == "en":
        return text

    return OUTPUT_TRANSLATIONS.get(normalized, {}).get(text, text)


def localize_workflow_result(result: dict, language: str | None) -> dict:
    localized = dict(result)

    context = dict(localized.get("context", {}))
    if "interaction_summary" in context:
        context["interaction_summary"] = translate_output_text(
            context["interaction_summary"],
            language,
        )
    localized["context"] = context

    translation = dict(localized.get("translation", {}))
    for key in ("translation_for_user", "translation_for_other_person"):
        if key in translation:
            translation[key] = translate_output_text(translation[key], language)
    localized["translation"] = translation

    response = dict(localized.get("response", {}))
    if "bridge_message" in response:
        response["bridge_message"] = translate_output_text(
            response["bridge_message"],
            language,
        )
    localized["response"] = response

    learning = dict(localized.get("learning", {}))
    if "reflection_question" in learning:
        learning["reflection_question"] = translate_output_text(
            learning["reflection_question"],
            language,
        )
    localized["learning"] = learning

    safety = dict(localized.get("safety", {}))
    if "guidance" in safety:
        safety["guidance"] = translate_output_text(safety["guidance"], language)
    localized["safety"] = safety

    localized["output_language"] = normalize_language(language)
    return localized


def detect_user_language(text: str | None) -> str:
    if not text or not text.strip():
        return "en"

    lowered = f" {text.lower()} "
    scores = {
        language: _score_terms(lowered, terms)
        for language, terms in LANGUAGE_HINTS.items()
    }

    if re.search(r"[ãõçáéíóúâêô]", lowered):
        scores["pt-BR"] += 2
    if re.search(r"[ñ¿¡]", lowered):
        scores["es"] += 2

    language, score = max(scores.items(), key=lambda item: item[1])
    return language if score > 0 else "en"


def is_likely_language(text: str, language: str | None) -> bool:
    normalized = normalize_language(language)
    lowered = f" {text.lower()} "

    if normalized == "en":
        return not (
            re.search(r"[ãõçáéíóúâêôñ¿¡]", lowered)
            or _score_terms(lowered, LANGUAGE_HINTS["pt-BR"]) >= 2
            or _score_terms(lowered, LANGUAGE_HINTS["es"]) >= 2
        )

    if normalized == "pt-BR":
        return (
            bool(re.search(r"[ãõçáéíóúâêô]", lowered))
            or _score_terms(lowered, LANGUAGE_HINTS["pt-BR"]) >= 1
        )

    if normalized == "es":
        return (
            bool(re.search(r"[ñ¿¡]", lowered))
            or _score_terms(lowered, LANGUAGE_HINTS["es"]) >= 1
        )

    return True


def _score_terms(text: str, terms: tuple[str, ...]) -> int:
    return sum(1 for term in terms if term in text)
