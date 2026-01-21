from core.llm_client import call_llm

"""
Question Generator Agent

Responsible for generating a single, role-specific interview question
based on difficulty level.
"""

ROLE_CONTEXT = {
    "backend": "Focus on APIs, databases, scalability, and system design.",
    "frontend": "Focus on UI performance, accessibility, and state management.",
    "data": "Focus on data modeling, pipelines, and analytics."
}

DIFFICULTY_CONTEXT = {
    "easy": "Ask a basic conceptual interview question.",
    "medium": "Ask a practical, scenario-based interview question.",
    "hard": "Ask a deep design or trade-off focused interview question."
}


def generate_question(role: str, difficulty: str) -> str:
    role_key = role.lower()
    difficulty_key = difficulty.lower()

    role_hint = ROLE_CONTEXT.get(role_key, "Focus on general software engineering concepts.")
    difficulty_hint = DIFFICULTY_CONTEXT.get(difficulty_key, "Ask a medium-difficulty interview question.")

    prompt = f"""
You are a professional technical interviewer.

Interview Context:
- Role Focus: {role_hint}
- Difficulty Level: {difficulty_hint}

Task:
Generate exactly ONE interview question.
Do not include explanations, answers, or formatting.
Return only the question text.
"""

    return call_llm(prompt).strip()

