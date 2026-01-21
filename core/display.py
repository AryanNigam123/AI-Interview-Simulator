def display_evaluation(evaluation: dict):
    print("\n=== Evaluation ===")
    print(f"Technical Accuracy : {evaluation['technical_accuracy']} / 5")
    print(f"Completeness       : {evaluation['completeness']} / 5")
    print(f"Clarity            : {evaluation['clarity']} / 5")
    print(f"Communication      : {evaluation['communication']} / 5")

    print("\nStrengths:")
    print(evaluation["strengths"])

    print("\nGaps:")
    print(evaluation["gaps"])


def display_feedback(feedback: dict):
    print("\n=== Feedback ===\n")
    print(feedback["overall_summary"].replace("\\n", "\n"))
