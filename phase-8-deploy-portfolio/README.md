# Phase 8: Deployment, Portfolio, Applications (Weeks 15-16)

**Goal:** turn your work into something a stranger can run and an employer can evaluate, and put it in front of employers. Applying continues from here until you have an offer.

## Topics

| Days | Topic | Practice |
|---|---|---|
| 1-2 | Wrap a model or pipeline in an API with FastAPI: routes, request/response models with Pydantic, error handling | `POST /ask` endpoint for your RAG project |
| 3 | Configuration: environment variables, no hard-coded secrets, `.env.example` | Audit all projects for leaked keys |
| 4-5 | Docker: Dockerfile, build, run, `.dockerignore`, why containers help | Containerize the API |
| 6 | Hosting a demo: Hugging Face Spaces, Render, Railway, or similar free tiers | Put one project online |
| 7 | Logging, health checks, rate limiting basics, cost controls | Add `/health` and request logging |
| 8-10 | **Project 4: capstone** (see `projects/README.md`) | Deployed app with tests and evaluation |
| 11-12 | Portfolio polish: READMEs, demo GIFs, profile README, pinned repos | Follow Part 7 of `docs/github-guide.md` |
| 13-14 | Interview practice, application batches, project walk-throughs | Mock interviews |

## Minimal FastAPI shape

```python
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Question(BaseModel):
    text: str

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/ask")
def ask(q: Question):
    return {"answer": "wire your pipeline in here"}
```

Run with `uvicorn main:app --reload`, then open `http://127.0.0.1:8000/docs` for the automatic API docs.

## Minimal Dockerfile shape

```dockerfile
FROM python:3.11-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
```

## Portfolio checklist (per project)

- [ ] README: problem, demo (screenshot or GIF), run instructions in 5 commands or fewer
- [ ] Architecture in a short list or diagram
- [ ] Evaluation results with real numbers and honest limitations
- [ ] Tests that run without paid API calls
- [ ] `.env.example` present, no secrets in history
- [ ] Clear commit history and at least one tagged release

## Application push

- Follow `docs/job-search.md`. Keep the application log updated.
- Tailor your resume's project bullets to each role.
- Use your support background for adjacent roles. It's a strength.
- After every interview, write down the questions you couldn't answer and study them the next day.

## Done when

- [ ] One project is live online with a link in its README
- [ ] All four projects pass the portfolio checklist
- [ ] Your GitHub profile README is written and your best four repos are pinned
- [ ] You've done at least two mock interviews out loud
- [ ] You've sent at least 40 tailored applications across the role families in `docs/job-search.md`
