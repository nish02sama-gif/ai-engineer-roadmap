# Phase 5: LLM APIs and Prompting (Weeks 9-10)

**Goal:** build reliable applications on top of a large language model, not just chat with one.

## Topics

| Days | Topic | Practice |
|---|---|---|
| 1 | API keys, `.env`, `python-dotenv`, calling the Messages API | `first_call.py` |
| 2 | System prompts, roles, multi-turn conversations, temperature, max tokens | Build a tiny chat loop |
| 3-4 | Prompt design: clear instructions, examples, format requirements, delimiting inputs | Rewrite one prompt five ways and compare |
| 5-6 | Structured output: JSON responses, validation with Pydantic, retries on bad output | Extract fields from messy text |
| 7-8 | Tool use (function calling): defining tools, handling tool calls, returning results | Give the model a calculator and a lookup tool |
| 9 | Cost, latency, caching, rate limits, streaming | Measure tokens and cost per request |
| 10 | Safety and reliability: prompt injection, hallucination, refusing gracefully | Test your app with hostile inputs |
| 11-14 | Project 1 (below), README, tests, push | Support Ticket Triage |

Start with the official documentation at docs.claude.com and the Anthropic Console. It is the most accurate source and stays current as models and features change. Also work through Anthropic's courses repo on GitHub (`anthropics/courses`).

## Setup

```bash
pip install -r requirements-llm.txt
cp .env.example .env        # then edit .env and add your key
python phase-5-llm-apis/first_call.py
```

Never paste your key into code or commit `.env`. See `docs/github-guide.md`, Part 4.

## Prompting habits that matter

- State the task, the audience, and the output format explicitly.
- Put the input inside clear delimiters (for example `<ticket>...</ticket>`) so instructions and data don't blur together.
- Show one or two examples of the output you want.
- Ask for JSON and **validate it in code**. Never trust the model to be well-formed every time.
- Change one thing at a time and keep a test set of inputs so you can tell whether a change helped.
- Treat any text from users or documents as untrusted. It can contain instructions you didn't write.

## Project 1: Support Ticket Triage

Full spec in `projects/README.md`. In short: given a raw support message, the app returns structured JSON (category, priority, sentiment, a short summary, a suggested reply draft), validates it, and handles failures. You'll write an evaluation set of at least 30 labelled tickets and report accuracy.

## Done when

- [ ] You've made API calls with system prompts, multi-turn history, and structured output
- [ ] Your code validates model output and retries or fails cleanly
- [ ] You've implemented at least one tool the model can call
- [ ] You can explain temperature, tokens, and context window to a non-technical person
- [ ] You can describe prompt injection and one way to reduce its risk
- [ ] Project 1 is pushed, runnable from the README, with tests that don't call the paid API (use mocks or saved responses)

## GitHub skill this phase

Part 5 of `docs/github-guide.md`: activate CI so your tests run on every push, and store the API key as an Actions secret only if a workflow truly needs it. Mock API calls in tests so CI stays free and fast.
