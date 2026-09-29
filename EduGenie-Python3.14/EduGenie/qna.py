from gemini_client import get_gemini_service


def answer_question(question: str) -> str:
    prompt = f"""
You are EduGenie, an accurate academic Q&A assistant.
Answer the student's question directly and concisely.
If the question is ambiguous, state the assumption you made.
For calculations or technical questions, show the essential reasoning steps.
If you are uncertain, say so instead of inventing facts.

Student question:
{question}
"""
    return get_gemini_service().generate(prompt, temperature=0.25, max_output_tokens=1000)
