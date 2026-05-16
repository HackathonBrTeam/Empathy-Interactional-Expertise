from empathy_engine.presentation.demo_scenarios import (
    demo_scenario_options,
    get_demo_scenario,
)


REQUIRED_FIELDS = {
    "label",
    "user_profile",
    "other_profile",
    "context_factors",
    "repair_supports",
    "interaction",
}


def test_demo_scenarios_exist_for_supported_languages():
    for language in ("pt-BR", "en", "es"):
        options = demo_scenario_options(language)

        assert options
        for scenario_id, label in options:
            scenario = get_demo_scenario(scenario_id, language)
            assert label == scenario["label"]
            assert REQUIRED_FIELDS <= set(scenario)
            assert all(scenario[field] for field in REQUIRED_FIELDS)
