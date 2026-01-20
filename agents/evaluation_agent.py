from core.llm_client import call_llm

def evaluate_answer(question, answer):
    prompt = f"""
    You are a technical interviewer.

    Interview Question:
    {question}

    Candidate Answer:
    {answer}

    Evaluate the answer and respond in this format:

    Score (0-10):
    Strengths:
    Missing Points:
    """
    
    return call_llm(prompt)
