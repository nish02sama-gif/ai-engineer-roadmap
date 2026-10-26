# 16-Week Roadmap

Assumes about 25 hours a week. If you have fewer hours, stretch each phase and keep the order. The order matters more than the speed.

| Weeks | Phase | You learn | You ship | GitHub skill |
|---|---|---|---|---|
| 1-2 | 1. Python core | Syntax, data structures, functions, files, JSON, classes, errors, virtual environments, pytest | `exercises.py` passing all tests; a small log-parsing CLI | init, add, commit, push, README, .gitignore |
| 3-4 | 2. Data libraries | NumPy, pandas, matplotlib, `requests`, REST APIs, SQL with SQLite | Ticket-data analysis report with charts | branches, pull requests, issues |
| 5-6 | 3. ML fundamentals | Train/test split, regression, classification, overfitting, metrics, scikit-learn pipelines | Ticket-category classifier with an honest evaluation | secrets hygiene, `git restore`, `git revert` |
| 7-8 | 4. NLP and deep learning | Tokenization, TF-IDF, embeddings, transformers, Hugging Face, PyTorch basics | Semantic search over a small FAQ set | notebooks in Git, tags |
| 9-10 | 5. LLM APIs | Messages API, system prompts, structured output, tool use, cost and latency, prompt iteration | Project 1: Support Ticket Triage | GitHub Actions CI, Actions secrets |
| 11-12 | 6. RAG | Chunking, embeddings, vector search, reranking, citations, failure modes | Project 2: Docs Q&A with citations | forks, open-source contribution |
| 13-14 | 7. Agents and evals | Tool-using agents, text-to-SQL, guardrails, evaluation sets, regression testing | Project 3: Data Analyst Agent | issues as a task board, code review |
| 15-16 | 8. Deploy and apply | FastAPI, Docker, environment config, logging, demo hosting | Project 4: deployed capstone; polished profile | profile README, releases, pinned repos |

## Weekly rhythm

- **Mon-Thu**: new material and exercises.
- **Fri**: build or extend the phase project.
- **Sat**: review, cleanup, write the weekly summary in `docs/progress-log.md`.
- **Sun**: rest, or light reading.

## Checkpoints (be honest with yourself)

- **End of week 2**: you can write a 50-line Python script without copying, and every function in `exercises.py` passes.
- **End of week 4**: you can take a CSV you've never seen, clean it, and answer three questions about it with charts.
- **End of week 6**: you can explain why accuracy alone can mislead, and why a train/test split exists.
- **End of week 10**: you have one LLM project that a stranger can run from your README.
- **End of week 12**: you can explain how RAG works on a whiteboard and name three ways it fails.
- **End of week 16**: four projects, each with a README, tests, and a short write-up of what went wrong and what you changed.

If a checkpoint is missed, spend a few extra days there before moving on. Gaps in the early phases cause pain later.

## What to do when you're stuck

1. Read the error message from the bottom up.
2. Make the smallest example that still fails.
3. Search the exact error text. Check the library's official docs.
4. Ask an AI assistant to explain the error, not to write the solution. Then write it yourself.
5. Time-box: if 45 minutes pass with no progress, ask for help with a clear description of what you tried.
