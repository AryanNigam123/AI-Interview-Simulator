from core.llm_client import call_llm

def generate_question(role, difficulty):
    prompt = f"""
    You are a professional interviewer.

    Role: {role}
    Difficulty: {difficulty}

    Ask ONE interview question.
    Only output the question.
    """

    return call_llm(prompt)
