# Portfolio Projects

Four projects, one per milestone. Each one lives in its own repository (or a clearly separated folder) with its own README. Build them in order because each reuses skills from the last.

## Project 1: Support Ticket Triage (Phase 5)

**Problem:** support teams receive messy free-text messages. Triage them automatically.

**What it does**
- Input: a raw ticket message.
- Output: validated JSON with `category`, `priority`, `sentiment`, `summary` (under 20 words), and a `suggested_reply` draft.
- Handles invalid model output with a retry, then a clean error.
- Treats the ticket text as untrusted input (prompt-injection test cases included).

**Tech:** Python, Claude API, Pydantic, pytest.

**Evaluation:** 30+ hand-labelled tickets. Report category accuracy, priority accuracy, and cost per ticket. Compare at least two prompt versions.

**Done when:** a stranger can clone it, add a key, and triage a ticket in five commands; tests run without API calls.

## Project 2: Docs Q&A with Citations (Phase 6)

**Problem:** answer questions from a document set and show where the answer came from.

**What it does**
- Loads documents, chunks them, embeds them, and stores the vectors.
- Retrieves the top chunks, prompts the model to answer only from them, and cites chunk sources.
- Says "I don't know" when the documents don't contain the answer.

**Tech:** Python, sentence-transformers, NumPy or a vector store (Chroma or FAISS), Claude API.

**Evaluation:** 40+ questions including 8 unanswerable ones. Report retrieval hit rate at top-3, answer accuracy, and refusal accuracy. Compare chunk sizes. Show three failures with a diagnosis.

**Done when:** README has the results table and an honest limitations section.

## Project 3: Data Analyst Agent (Phase 7)

**Problem:** let a non-technical person ask questions of a database in plain English.

**What it does**
- Reads the schema, writes a read-only SQL query, runs it with a row limit, and explains the result, showing the SQL.
- Rejects anything that isn't a SELECT, and refuses unanswerable questions.
- Logs every step, token count, and latency.

**Tech:** Python, SQLite (use your Phase 2 ticket data or a sample database), Claude API with tool use.

**Evaluation:** 40+ cases including ambiguous and adversarial ones. Report accuracy by question type and cost per question. Issues on GitHub for every failure, fixed via PRs.

**Done when:** the evaluation numbers improved between version 1 and version 2, and the README shows both.

## Project 4: Support Copilot Capstone (Phase 8)

**Problem:** help a support agent resolve tickets faster by combining everything.

**What it does**
- A web API (FastAPI) and a simple front end (or a Hugging Face Space with Gradio or Streamlit).
- Given a ticket, it triages it (Project 1), retrieves relevant help-article passages with citations (Project 2), and drafts a reply grounded in those passages.
- Optional: an analytics tool using Project 3 to answer "how many similar tickets this week?"
- Containerized with Docker, deployed with a public demo link.

**Tech:** FastAPI, Docker, everything above.

**Evaluation:** end-to-end test set of 30 tickets, scored for correct category, helpful grounded answer, and no invented policy. Include a cost and latency summary.

**Done when:** a recruiter can open the demo link, try it in under a minute, and read a README that explains the design and its limits.

## README template for every project

```
# Project name
One sentence on the problem it solves.

## Demo
Screenshot or GIF, plus a live link if deployed.

## How it works
Short architecture list or diagram.

## Run it
5 commands or fewer.

## Evaluation
Table of results, how the test set was made, what failed.

## Limitations and next steps
What you would improve and what you would not trust it with.
```

## Honest-claims rule

In your README and on your resume, state only what the evaluation supports. "87% category accuracy on 60 hand-labelled tickets" is believable and impressive. "Production-ready AI system" is not.
