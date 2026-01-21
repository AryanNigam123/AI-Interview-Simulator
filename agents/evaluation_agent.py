from core.llm_client import call_llm
import json

"""
Evaluation Agent

Evaluates a candidate answer using a predefined rubric
and returns structured, explainable scores.
"""

EVALUATION_RUBRIC = {
    "technical_accuracy": "Correctness of concepts and reasoning",
    "completeness": "Coverage of key aspects expected in an ideal answer",
    "clarity": "Logical flow and structure",
    "communication": "Confidence, conciseness, and relevance"
}


def evaluate_answer(question: str, answer: str) -> dict:
    if not answer or len(answer.strip()) < 10:
        return {
            "technical_accuracy": 0,
            "completeness": 0,
            "clarity": 0,
            "communication": 0,
            "strengths": "Answer is too short to evaluate.",
            "gaps": "Insufficient explanation provided."
        }

    prompt = f"""
You are a technical interviewer evaluating a candidate answer.

Question:
{question}

Candidate Answer:
{answer}

Evaluation Rubric (score each from 0 to 5):
- technical_accuracy: Correctness of concepts and reasoning
- completeness: Coverage of key aspects
- clarity: Logical structure and flow
- communication: Confidence and relevance

Instructions:
- Return ONLY valid JSON
- Scores must be integers between 0 and 5
- Provide short text for strengths and gaps
- Do NOT include explanations outside JSON

Expected JSON format:
{{
  "technical_accuracy": 0,
  "completeness": 0,
  "clarity": 0,
  "communication": 0,
  "strengths": "",
  "gaps": ""
}}
"""

    response = call_llm(prompt).strip()
    return json.loads(response)
