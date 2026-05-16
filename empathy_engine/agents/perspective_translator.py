from empathy_engine.schemas import PerspectiveTranslation


class PerspectiveTranslatorAgent:

    def run(self, analysis) -> PerspectiveTranslation:
        if getattr(analysis, "gap_type", "") == "information_clarity_mismatch":
            return PerspectiveTranslation(
                translation_for_user=(
                    "The other person may not realize which project details feel "
                    "unclear, incomplete, or out of order."
                ),
                translation_for_other_person=(
                    "The user may need the project information organized into "
                    "clear points, priorities, and next steps."
                ),
            )

        return PerspectiveTranslation(
            translation_for_user=(
                "The other person may expect more emotional cues."
            ),
            translation_for_other_person=(
                "Direct language may reflect efficiency, not hostility."
            )
        )
