from agents.question_agent import generate_question
from agents.evaluation_agent import evaluate_answer
from agents.feedback_agent import generate_feedback

def main():
    role = input("Enter role (e.g. Software Engineer): ")
    difficulty = input("Enter difficulty (easy / medium / hard): ")

    question = generate_question(role, difficulty)
    print("\nInterview Question:")
    print(question)

    answer = input("\nYour Answer: ")

    evaluation = evaluate_answer(question, answer)
    print("\nEvaluation:")
    print(evaluation)

    feedback = generate_feedback(evaluation)
    print("\nFinal Feedback:")
    print(feedback)

if __name__ == "__main__":
    main()