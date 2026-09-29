from pydantic import BaseModel, Field


class TextRequest(BaseModel):
    text: str = Field(min_length=1, max_length=30000)


class QARequest(TextRequest):
    pass


class ExplainRequest(TextRequest):
    level: str = Field(default="beginner", max_length=30)


class QuizRequest(TextRequest):
    count: int = Field(default=3, ge=1, le=10)


class QuizQuestion(BaseModel):
    question: str
    options: list[str] = Field(min_length=4, max_length=4)
    answer: str
    explanation: str = ""


class QuizResponse(BaseModel):
    questions: list[QuizQuestion]


class LearningPathRequest(TextRequest):
    level: str = Field(default="beginner", max_length=30)
    weeks: int = Field(default=6, ge=1, le=52)


class APIResponse(BaseModel):
    result: str
