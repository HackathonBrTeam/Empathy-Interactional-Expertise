from empathy_engine.schemas import DoubleEmpathyAnalysis


class DoubleEmpathyAnalyzerAgent:

    def run(self, context) -> DoubleEmpathyAnalysis:
        if getattr(context, "communication_need", "") == "clarify_project_information":
            return DoubleEmpathyAnalysis(
                gap_type="information_clarity_mismatch",
                possible_misinterpretation=(
                    "Information shared without enough structure may be read as "
                    "confusing or uncooperative, while the other person may be "
                    "responding under uncertainty or with a different sense of "
                    "what context is necessary."
                ),
                mutual_need=(
                    "Make the project information explicit, ordered, and checkable "
                    "without assigning blame."
                ),
            )

        return DoubleEmpathyAnalysis(
            gap_type="tone_expectation_mismatch",
            possible_misinterpretation=(
                "Directness perceived as hostility"
            ),
            mutual_need=(
                "Clarify intention and ask what would make the exchange easier "
                "for both people."
            ),
        )
