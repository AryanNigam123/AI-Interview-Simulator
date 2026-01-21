from core.llm_client import call_llm

"""
Feedback Agent

Converts structured evaluation output into
clear, actionable interview feedback.
"""


def generate_feedback(evaluation: dict) -> dict:
    prompt = f"""
You are an experienced technical interviewer providing feedback.

Evaluation Scores:
- Technical Accuracy: {evaluation["technical_accuracy"]}/5
- Completeness: {evaluation["completeness"]}/5
- Clarity: {evaluation["clarity"]}/5
- Communication: {evaluation["communication"]}/5

Identified Strengths:
{evaluation["strengths"]}

Identified Gaps:
{evaluation["gaps"]}

Instructions:
- Be constructive and encouraging
- Do NOT repeat numeric scores
- Focus on improvement, not judgment
- Return feedback in plain text sections

Provide:
1. Overall Summary (2–3 sentences)
2. Key Strengths
3. Areas to Improve
4. Suggested Next Steps
"""

    response = call_llm(prompt).strip()

    return {
        "overall_summary": response
    }
