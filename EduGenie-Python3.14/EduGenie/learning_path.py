from gemini_client import get_gemini_service


def get_learning_recommendations(topic: str, level: str = "beginner", weeks: int = 6) -> str:
    prompt = f"""
Create a personalized {weeks}-week learning path for: {topic}
Learner level: {level}

Structure it from fundamentals to more advanced material.
For each week include: goals, topics, a small practice task, and suggested resource
TYPES (video, article, documentation, book). Do not invent URLs. If naming a resource,
prefer well-known official documentation or broadly recognizable resources.
End with a simple self-check checklist.
"""
    return get_gemini_service().generate(prompt, temperature=0.45, max_output_tokens=1800)
