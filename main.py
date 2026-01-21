from agents.question_agent import generate_question
from agents.evaluation_agent import evaluate_answer
from agents.feedback_agent import generate_feedback
from core.display import display_evaluation, display_feedback


def main():
    role = input("Enter role (e.g. Software Engineer): ")
    difficulty = input("Enter difficulty (easy / medium / hard): ")

    question = generate_question(role, difficulty)
    print("\nInterview Question:")
    print(question)

    answer = input("\nYour Answer: ")

    evaluation = evaluate_answer(question, answer)
    display_evaluation(evaluation)

    feedback = generate_feedback(evaluation)
    display_feedback(feedback)


if __name__ == "__main__":
    main()
