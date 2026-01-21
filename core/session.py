from typing import List, Dict


class InterviewSession:
    """
    Maintains state for a multi-round interview session.
    Stored in-memory by design (no persistence).
    """

    def __init__(self, role: str, difficulty: str):
        self.role = role
        self.difficulty = difficulty
        self.rounds: List[Dict] = []

    def add_round(self, question: str, evaluation: dict):
        self.rounds.append({
            "question": question,
            "evaluation": evaluation
        })

    def average_scores(self) -> Dict[str, float]:
        if not self.rounds:
            return {}

        keys = [
            "technical_accuracy",
            "completeness",
            "clarity",
            "communication"
        ]

        # 🔧 FIXED PART (no dict comprehension)
        totals = {}
        for key in keys:
            totals[key] = 0

        # Aggregate scores from each round
        for round_data in self.rounds:
            evaluation = round_data["evaluation"]
            for key in keys:
                totals[key] += evaluation.get(key, 0)

        # Compute averages
        averages = {}
        for key in keys:
            averages[key] = round(totals[key] / len(self.rounds), 2)

        return averages
