from schemas import QuizResponse
from gemini_client import get_gemini_service
from utils import parse_json


def generate_quiz(text: str, count: int = 3) -> QuizResponse:
    prompt = f"""
Create exactly {count} multiple-choice questions from the passage/topic below.
Return ONLY valid JSON with this exact shape:
{{
  "questions": [
    {{
      "question": "...",
      "options": ["A", "B", "C", "D"],
      "answer": "the exact correct option text",
      "explanation": "brief reason"
    }}
  ]
}}
Rules: exactly four options per question; exactly one correct answer; questions must
be answerable from the provided content; plausible distractors; no Markdown fences.

Content:
{text}
"""
    raw = get_gemini_service().generate(
        prompt,
        temperature=0.55,
        max_output_tokens=1800,
        response_mime_type="application/json",
    )
    data = parse_json(raw)
    return QuizResponse.model_validate(data)
