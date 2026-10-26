# Phase 7: Agents and Evaluation (Weeks 13-14)

**Goal:** build an LLM system that can take actions with tools, and prove with evidence that it works. Evaluation is the skill that separates people who can demo from people who can ship.

## Topics

| Days | Topic | Practice |
|---|---|---|
| 1-2 | What an agent is: a loop where the model chooses a tool, you run it, and you return the result until done | Write the loop yourself in under 60 lines |
| 3-4 | Designing tools: clear names, descriptions, input schemas, safe defaults, errors the model can act on | Build 3 tools: search docs, run SQL (read-only), calculator |
| 5-6 | Text-to-SQL: giving the model a schema, validating queries, read-only connections, row limits | Answer questions about the Phase 2 ticket data via SQL |
| 7 | Guardrails: allow-lists, maximum steps, timeouts, human confirmation for risky actions, logging every tool call | Add a step limit and a query allow-list |
| 8-9 | Evaluation: building test sets, exact-match and rubric checks, LLM-as-judge and its biases, regression tests | 40-case eval with a results table |
| 10 | Observability: log prompts, tool calls, token usage, latency, cost | Write a JSON log for every run |
| 11-14 | Project 3 (below), README, push | Data Analyst Agent |

## Principles

- **Start without an agent.** If a fixed pipeline solves it (like Phase 5 or Phase 6), use that. Agents add flexibility and also failure modes.
- **Constrain tools.** The database connection is read-only. File tools can touch one folder. Anything destructive asks a human first.
- **Cap the loop.** Maximum number of steps, maximum tokens, and a timeout.
- **Log everything.** When an agent does something strange, the log is how you find out why.
- **Every change gets re-evaluated.** Run your test set before and after, and keep the numbers.

## Project 3: Data Analyst Agent

Full spec in `projects/README.md`. A user asks a plain-English question about a SQLite database; the agent inspects the schema, writes a read-only SQL query, runs it, and explains the result with the query shown. It refuses to modify data and says so when the question can't be answered from the schema.

## Evaluation set (required)

Create `eval/cases.json` with at least 40 questions, each with the expected answer or a check function. Include:

- easy lookups, aggregations, and joins
- questions with ambiguous wording
- questions the data cannot answer
- adversarial inputs ("delete all tickets", prompt injection in a text column)

Report: accuracy overall and by type, number of tool calls per question, average cost per question, and the three worst failures with a diagnosis.

## Done when

- [ ] You've written an agent loop by hand, with a step limit and logging
- [ ] The agent's SQL runs on a read-only connection and rejects anything but SELECT
- [ ] You have an evaluation set and a results table, and you improved a number you can show
- [ ] You can explain LLM-as-judge and one reason it can mislead you
- [ ] Project 3 is pushed with a README that includes the evaluation results

## GitHub skill this phase

Use **Issues** as your task board: one issue per failure found by the evaluation, fixed by a PR that references it (`Fixes #12`). Add a GitHub Project board for the four portfolio projects.
