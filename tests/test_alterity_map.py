from empathy_engine.presentation.alterity_map import (
    compose_alterity_map_context,
    compose_interaction_with_alterity_map,
)


def test_compose_alterity_map_context_omits_empty_fields():
    context = compose_alterity_map_context(
        {
            "user_profile": "Direct and literal.",
            "other_profile": "",
            "context_factors": "Noisy room.",
            "repair_supports": "  ",
        }
    )

    assert "Alterity map registered" in context
    assert "User communication profile: Direct and literal." in context
    assert "Sensory or contextual factors: Noisy room." in context
    assert "Other person's possible" not in context


def test_compose_interaction_with_alterity_map_keeps_interaction_when_empty():
    interaction = compose_interaction_with_alterity_map(
        "My message was misunderstood.",
        {"user_profile": ""},
    )

    assert interaction == "My message was misunderstood."


def test_compose_interaction_with_alterity_map_adds_context_before_interaction():
    interaction = compose_interaction_with_alterity_map(
        "My message was misunderstood.",
        {"repair_supports": "Ask what would help."},
    )

    assert interaction.startswith("Alterity map registered")
    assert "Interaction to analyze:\nMy message was misunderstood." in interaction
