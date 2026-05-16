from empathy_engine.schemas import ContextResult


class ContextDecoderAgent:

    def run(self, interaction: str) -> ContextResult:
        lowered = interaction.lower()
        observed_cues = []

        if any(term in lowered for term in ("confusa", "confuso", "confusing")):
            observed_cues.append("confusing_information")
        if any(term in lowered for term in ("desorganizada", "desorganizado", "disorganized")):
            observed_cues.append("disorganized_information")
        if any(term in lowered for term in ("projeto", "project")):
            observed_cues.append("project_context")
        if any(term in lowered for term in ("atrasado", "atrasada", "late", "delayed")):
            observed_cues.append("time_pressure")
        if any(term in lowered for term in ("rígida", "rigida", "rígido", "rigido", "rigid")):
            observed_cues.append("perceived_rigidity")

        if {"confusing_information", "disorganized_information"} & set(observed_cues):
            return ContextResult(
                literal_language=True,
                ambiguity_level="high",
                interaction_summary=(
                    "The exchange is about project information that the user "
                    "experiences as confusing or disorganized."
                ),
                communication_need="clarify_project_information",
                observed_cues=observed_cues,
            )

        return ContextResult(
            literal_language=True,
            ambiguity_level="medium",
            interaction_summary=(
                "The exchange may involve a mismatch in tone expectations or "
                "communication cues."
            ),
            communication_need="clarify_intention",
            observed_cues=observed_cues,
        )
