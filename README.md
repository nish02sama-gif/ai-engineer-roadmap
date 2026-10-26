# AI Engineer Roadmap

A hands-on, 16-week path from "a little Python" to a GitHub portfolio that supports applications for entry-level AI roles. You learn Python, the data and ML libraries, NLP, LLM APIs, RAG, agents, and deployment, and you learn Git and GitHub along the way by using them every day.

## How this repo works

- Each **phase** is a folder with its own README: goals, topics, resources, exercises, and a "done when" checklist.
- Every phase ends with something you **commit to GitHub**. By week 16 your profile shows steady daily work and four real projects.
- You learn by writing code and getting feedback, not by watching videos. Videos are optional; official docs and exercises come first.

```
ai-engineer-roadmap/
├── ROADMAP.md                    # week-by-week plan
├── docs/
│   ├── github-guide.md           # Git + GitHub from zero, tied to each phase
│   ├── job-search.md             # roles to target, resume, portfolio, interviews
│   ├── resources.md              # curated free resources
│   ├── progress-log.md           # daily/weekly log template
│   └── templates/tests.yml       # CI workflow you'll activate in Phase 5
├── phase-1-python/               # Python core + testing + Git basics
├── phase-2-data-libraries/       # NumPy, pandas, matplotlib, APIs, SQL
├── phase-3-ml-fundamentals/      # scikit-learn, evaluation
├── phase-4-nlp-deep-learning/    # text processing, embeddings, transformers
├── phase-5-llm-apis/             # LLM APIs, prompting, structured output, tool use
├── phase-6-rag/                  # retrieval-augmented generation
├── phase-7-agents-evals/         # agents, evaluation, guardrails
├── phase-8-deploy-portfolio/     # FastAPI, Docker, polish, applying
├── projects/                     # the four portfolio projects
├── requirements.txt              # core libraries
├── requirements-llm.txt          # heavier libraries (Phase 4+)
└── .env.example                  # copy to .env, never commit .env
```

## Day 1 setup (about 1 hour)

1. Install **Python 3.11+**, **Git**, and **VS Code**.
2. Create a free **GitHub** account and turn on two-factor authentication.
3. In a terminal, from this folder:

```bash
python -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

4. Follow **Part 1 of `docs/github-guide.md`** to turn this folder into your own repo and push it.
5. Open `phase-1-python/README.md` and start.

## Daily routine (about 5 hours)

| Block | Time | What |
|---|---|---|
| Learn | 1.5 h | Read or follow the docs and course for the current topic |
| Build | 2.5 h | Write code: exercises, then the phase project |
| Review | 30 min | Re-do what you got wrong, write notes in your own words |
| Ship | 30 min | Commit, push, update `docs/progress-log.md` |

One rule matters most: **push something every day**, even small. Consistent commits show employers you actually code.

## Progress tracker

- [ ] Phase 1: Python core, tests, Git basics (weeks 1-2)
- [ ] Phase 2: NumPy, pandas, matplotlib, APIs, SQL (weeks 3-4)
- [ ] Phase 3: ML fundamentals with scikit-learn (weeks 5-6)
- [ ] Phase 4: NLP and deep learning basics (weeks 7-8)
- [ ] Phase 5: LLM APIs and prompting (weeks 9-10)
- [ ] Phase 6: RAG (weeks 11-12)
- [ ] Phase 7: Agents and evaluation (weeks 13-14)
- [ ] Phase 8: Deployment, portfolio, applications (weeks 15-16)

Start applying around **week 9**, not week 16. See `docs/job-search.md`.
