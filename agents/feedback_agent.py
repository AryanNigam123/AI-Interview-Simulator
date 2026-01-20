from core.llm_client import call_llm

def generate_feedback(evaluation_text):
    prompt = f"""
    You are a supportive interview coach.

    Based on the following evaluation, generate clear and concise feedback
    for the candidate.

    Evaluation:
    {evaluation_text}

    Respond in this format:

    Overall Feedback:
    Key Improvement Areas:
    Next Steps:
    """

    return call_llm(prompt)
