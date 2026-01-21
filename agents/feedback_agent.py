from core.llm_client import call_llm

"""
Feedback Agent

Converts structured evaluation output into
clear, actionable interview feedback.
"""


def generate_feedback(evaluation: dict) -> dict:
    # Guard: evaluation failure
    if (
        evaluation.get("technical_accuracy") == 0
        and "failed" in evaluation.get("strengths", "").lower()
    ):
        return {
            "overall_summary": (
                "The system could not reliably evaluate the response. "
                "Please try again with a more detailed answer."
            )
        }

    prompt = f"""
You are an experienced technical interviewer providing feedback.

Evaluation Summary:
- Technical Accuracy: {evaluation.get("technical_accuracy", 0)}/5
- Completeness: {evaluation.get("completeness", 0)}/5
- Clarity: {evaluation.get("clarity", 0)}/5
- Communication: {evaluation.get("communication", 0)}/5

Identified Strengths:
{evaluation.get("strengths", "")}

Identified Gaps:
{evaluation.get("gaps", "")}

Instructions:
- Be constructive and encouraging
- Do NOT repeat numeric scores
- Focus on improvement, not judgment
- Avoid technical jargon unless necessary
- Return clear, concise feedback

Provide:
1. Overall Summary (2–3 sentences)
2. Key Strengths
3. Areas to Improve
4. Suggested Next Steps
"""

    response = call_llm(prompt)

    if not response:
        return {
            "overall_summary": (
                "Feedback could not be generated at this time. "
                "Please try again later."
            )
        }

    return {
        "overall_summary": response.strip()
    }
