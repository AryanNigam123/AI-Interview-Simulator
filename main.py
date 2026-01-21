from agents.question_agent import generate_question
from agents.evaluation_agent import evaluate_answer
from agents.feedback_agent import generate_feedback
from core.session import InterviewSession
from core.display import display_evaluation, display_feedback


def main():
    role = input("Enter role (e.g. Software Engineer): ")
    difficulty = input("Enter difficulty (easy / medium / hard): ")

    session = InterviewSession(role, difficulty)

    ROUNDS = 3

    for i in range(ROUNDS):
        print(f"\n--- Interview Round {i + 1} ---")

        question = generate_question(role, difficulty)
        print("\nInterview Question:")
        print(question)

        answer = input("\nYour Answer: ")

        evaluation = evaluate_answer(question, answer)
        session.add_round(question, evaluation)

        display_evaluation(evaluation)

    # Session summary
    print("\n=== Session Summary ===")
    averages = session.average_scores()

    for k, v in averages.items():
        print(f"{k.replace('_', ' ').title()}: {v} / 5")

    # Optional session-level feedback
    feedback = generate_feedback({
        **averages,
        "strengths": "Aggregated strengths across interview rounds.",
        "gaps": "Recurring gaps identified across interview rounds."
    })

    display_feedback(feedback)


if __name__ == "__main__":
    main()
