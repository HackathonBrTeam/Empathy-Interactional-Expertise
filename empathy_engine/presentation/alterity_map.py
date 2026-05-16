ALTERITY_MAP_FIELD_LABELS = {
    "user_profile": "User communication profile",
    "other_profile": "Other person's possible communication profile",
    "context_factors": "Sensory or contextual factors",
    "repair_supports": "Supports that may help repair the exchange",
}


def compose_alterity_map_context(alterity_map: dict[str, str]) -> str:
    entries = [
        (label, _clean(value))
        for key, label in ALTERITY_MAP_FIELD_LABELS.items()
        if (value := alterity_map.get(key))
    ]

    if not entries:
        return ""

    lines = ["Alterity map registered for this analysis:"]
    lines.extend(f"- {label}: {value}" for label, value in entries)
    return "\n".join(lines)


def compose_interaction_with_alterity_map(
    interaction: str,
    alterity_map: dict[str, str],
) -> str:
    alterity_context = compose_alterity_map_context(alterity_map)
    clean_interaction = _clean(interaction)

    if not alterity_context:
        return clean_interaction

    return f"{alterity_context}\n\nInteraction to analyze:\n{clean_interaction}"


def _clean(value: str | None) -> str:
    return " ".join((value or "").split())
