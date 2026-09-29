from gemini_client import get_gemini_service


def explain_concept(topic: str, level: str = "beginner") -> str:
    prompt = f"""
You are EduGenie, a friendly educational tutor.
Explain the topic below for a {level} learner.
Use simple language, short sections, one relatable example, and a short recap.
Do not assume advanced prior knowledge.

Topic:
{topic}
"""
    return get_gemini_service().generate(prompt, temperature=0.35, max_output_tokens=900)
