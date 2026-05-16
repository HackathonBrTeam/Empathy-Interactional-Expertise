from empathy_engine.presentation.learning_diary import (
    diary_entry_title,
    display_bridge_for_language,
    display_feedback_for_language,
    extract_diary_interaction,
)


def test_extract_diary_interaction_hides_internal_alterity_context():
    text = (
        "[PERSON] map registered for this analysis:\n"
        "- [PERSON] communication profile: direto\n\n"
        "[PERSON] to analyze: meu colega achou minha mensagem grosseira"
    )

    assert (
        extract_diary_interaction(text)
        == "meu colega achou minha mensagem grosseira"
    )


def test_extract_diary_interaction_hides_person_marker_without_context_block():
    text = "[PERSON] colega compartilhou informacoes confusas."

    assert extract_diary_interaction(text) == "colega compartilhou informacoes confusas."


def test_display_bridge_for_language_uses_embedded_portuguese_section():
    bridge = (
        "Here's a concise, neutral bridge:\n\n"
        "It seems like there might be a difference.\n\n"
        "Brazilian Portuguese:\n\n"
        "Parece que pode haver uma diferenca na forma como cada um prefere se expressar."
    )

    displayed = display_bridge_for_language(bridge, "pt-BR")

    assert displayed.startswith("Parece que pode haver")
    assert "Here's" not in displayed


def test_display_bridge_for_language_uses_portuguese_translation_section():
    bridge = (
        "Here’s a concise, non-diagnostic empathy bridge:\n\n"
        "Could we clarify what is currently unclear?\n\n"
        "---\n\n"
        "Brazilian Portuguese Translation:\n\n"
        "Vamos dar uma olhada rapida para esclarecer o que esta confuso?"
    )

    displayed = display_bridge_for_language(bridge, "pt-BR")

    assert displayed == "Vamos dar uma olhada rapida para esclarecer o que esta confuso?"
    assert "Here’s" not in displayed
    assert "Brazilian Portuguese" not in displayed


def test_display_bridge_for_language_keeps_plain_text_when_no_section_exists():
    bridge = "Clarify intention and ask what would help."

    assert display_bridge_for_language(bridge, "pt-BR") == bridge


def test_display_feedback_for_language_localizes_stored_values():
    assert display_feedback_for_language("useful_safe", "pt-BR") == "Útil e segura"
    assert display_feedback_for_language("partially_useful", "es") == "Parcialmente útil"
    assert display_feedback_for_language("not_useful", "en") == "Not useful"
    assert display_feedback_for_language(None, "pt-BR") == "sem feedback"


def test_diary_entry_title_uses_interaction_summary_and_local_date():
    title = diary_entry_title(
        "[PERSON] to analyze: meu colega achou minha mensagem grosseira",
        "2026-05-16T03:50:24.528010+00:00",
        "pt-BR",
        "America/Sao_Paulo",
    )

    assert title == "meu colega achou minha mensagem grosseira - 16/05/2026 00:50"
