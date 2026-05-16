from empathy_engine.schemas import LearningResult


class LearningCoachAgent:

    def run(self, interaction) -> LearningResult:
        context = {}
        if hasattr(interaction, "context"):
            context = interaction.context
        elif isinstance(interaction, dict):
            context = interaction.get("context", {})

        communication_need = (
            getattr(context, "communication_need", "")
            if context
            else ""
        )

        if communication_need == "clarify_project_information":
            return LearningResult(
                reflection_question=(
                    "Which project information needs to be clarified first: "
                    "priority, deadline, responsibility, or next step?"
                )
            )

        return LearningResult(
            reflection_question=(
                "What assumptions existed in this interaction?"
            )
        )
