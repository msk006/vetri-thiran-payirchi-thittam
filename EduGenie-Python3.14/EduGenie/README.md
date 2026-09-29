# EduGenie — Google Gemini Powered Learning Assistant

EduGenie is a lightweight educational assistant implemented with FastAPI and a simple HTML/CSS/JavaScript frontend. It supports the modules described in the supplied project document: Q&A, concept explanation, quiz generation, summarization, and personalized learning paths.

## Python 3.14 note

This implementation targets **Python 3.14**. The supplied document describes Python 3.10+ and a local LaMini-Flan-T5 model for explanations. For a clean Python 3.14 setup, this build uses the current Google GenAI SDK for all five AI modules instead of adding the older PyTorch/Transformers local-model stack. This avoids making Python 3.14 depend on a local ML stack that may have platform-specific binary compatibility issues.

The API/module boundaries still follow the document's architecture: `explanation_module.py`, `qna.py`, `quiz_module.py`, `summary_module.py`, and `learning_path.py`.

## Project structure

```text
EduGenie/
├── main.py
├── config.py
├── gemini_client.py
├── explanation_module.py
├── qna.py
├── quiz_module.py
├── summary_module.py
├── learning_path.py
├── schemas.py
├── utils.py
├── requirements.txt
├── pyproject.toml
├── .env.example
├── .gitignore
├── templates/
│   └── index.html
├── static/
│   ├── app.js
│   └── style.css
└── tests/
    └── test_utils.py
```

## 1. Install Python 3.14

Verify:

```powershell
python --version
```

It should report Python 3.14.x.

## 2. Open the project in VS Code

Open the `EduGenie` folder in VS Code.

Open **Terminal → New Terminal**.

## 3. Create a virtual environment

Windows PowerShell:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

If PowerShell blocks activation, use Command Prompt:

```bat
.venv\Scripts\activate.bat
```

## 4. Install dependencies

```powershell
python -m pip install --upgrade pip
pip install -r requirements.txt
```

## 5. Create your Gemini API key

Create a Gemini API key in Google AI Studio, then copy `.env.example` to `.env` and put the key in:

```text
GEMINI_API_KEY=your_real_key_here
```

Never commit `.env` or expose the key in frontend JavaScript.

## 6. Run the application

```powershell
uvicorn main:app --reload
```

Open:

```text
http://127.0.0.1:8000
```

API documentation is available at `/docs`.

## 7. Test the API

Health check:

```powershell
curl http://127.0.0.1:8000/health
```

Q&A example:

```powershell
curl -X POST http://127.0.0.1:8000/qa -H "Content-Type: application/json" -d '{"text":"What is photosynthesis?"}'
```

Quiz example:

```powershell
curl -X POST http://127.0.0.1:8000/quiz -H "Content-Type: application/json" -d '{"text":"The water cycle includes evaporation, condensation and precipitation.","count":3}'
```

## 8. Run unit tests

```powershell
python -m pytest
```

## Endpoints

- `POST /qa`
- `POST /explain`
- `POST /quiz`
- `POST /summarize`
- `POST /learn/recommendations`
- `GET /health`
- `GET /docs`

## Troubleshooting

### `GEMINI_API_KEY is not configured`
Make sure the file is named exactly `.env`, is in the project root, and contains `GEMINI_API_KEY=...`.

### API quota or authentication error
Check the Gemini API key and its quota in Google AI Studio.

### PowerShell execution policy error
Use Command Prompt for activation or activate the environment using the Python executable directly.

### Port already in use
Run:

```powershell
uvicorn main:app --reload --port 8001
```

Then open `http://127.0.0.1:8001`.
