from pathlib import Path

from fastapi import FastAPI, HTTPException, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from config import get_settings
from explanation_module import explain_concept
from learning_path import get_learning_recommendations
from qna import answer_question
from quiz_module import generate_quiz
from schemas import (
    APIResponse,
    ExplainRequest,
    LearningPathRequest,
    QARequest,
    QuizRequest,
    QuizResponse,
    TextRequest,
)
from summary_module import summarize_text

BASE_DIR = Path(__file__).resolve().parent
settings = get_settings()

app = FastAPI(
    title=settings.app_name,
    version=settings.app_version,
    description="Google Gemini powered learning assistant based on the EduGenie project document.",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.cors_origin_list,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.mount("/static", StaticFiles(directory=BASE_DIR / "static"), name="static")
templates = Jinja2Templates(directory=BASE_DIR / "templates")


def run_module(fn, *args, **kwargs):
    try:
        return fn(*args, **kwargs)
    except Exception as exc:
        raise HTTPException(status_code=502, detail=str(exc)) from exc


@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@app.get("/health")
async def health():
    return {"status": "ok", "service": settings.app_name, "model": settings.gemini_model}


@app.post("/qa", response_model=APIResponse)
async def qa(request: QARequest):
    return APIResponse(result=run_module(answer_question, request.text))


@app.post("/explain", response_model=APIResponse)
async def explain(request: ExplainRequest):
    return APIResponse(result=run_module(explain_concept, request.text, request.level))


@app.post("/quiz", response_model=QuizResponse)
async def quiz(request: QuizRequest):
    return run_module(generate_quiz, request.text, request.count)


@app.post("/summarize", response_model=APIResponse)
async def summarize(request: TextRequest):
    return APIResponse(result=run_module(summarize_text, request.text))


@app.post("/learn/recommendations", response_model=APIResponse)
async def recommendations(request: LearningPathRequest):
    return APIResponse(
        result=run_module(
            get_learning_recommendations,
            request.text,
            request.level,
            request.weeks,
        )
    )
