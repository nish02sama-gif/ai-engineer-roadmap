# Phase 2: Data Libraries (Weeks 3-4)

**Goal:** take messy tabular data, clean it, analyze it, and show the result with charts. Almost every AI job touches data first.

## Topics

| Days | Topic | Practice |
|---|---|---|
| 1-2 | NumPy: arrays, shapes, vectorized math, broadcasting | Replace Python loops with array operations |
| 3-5 | pandas: DataFrame, selecting, filtering, `groupby`, `merge`, missing values, dates | `explore_tickets.py` tasks |
| 6 | matplotlib: line, bar, histogram, labelling | Charts for each finding |
| 7 | Jupyter notebooks: when to use them, how not to leave them messy | Re-do one analysis as a notebook |
| 8-9 | `requests`, REST APIs, JSON, status codes, headers, API keys | Pull data from a public API into a DataFrame |
| 10-12 | SQL with SQLite: SELECT, WHERE, JOIN, GROUP BY, window functions, `sqlite3` and `pandas.read_sql` | Load the ticket data into SQLite and re-answer the same questions in SQL |
| 13-14 | Project (below), cleanup, push | Ticket analysis report |

## Start here

`explore_tickets.py` generates a fake support-ticket dataset (no download needed), then runs a small analysis. Run it, read every line, then do the **Your turn** tasks at the bottom.

```bash
python phase-2-data-libraries/explore_tickets.py
```

## Project: ticket analysis report

Using the generated dataset (or a public dataset you pick from Kaggle), answer at least five questions and present each with a chart. Example questions:

1. Which categories get the most tickets, and which take longest to resolve?
2. Does resolution time change by weekday or hour?
3. Which priority level breaches a target (say 24 hours) most often?
4. Are there outliers, and what explains them?
5. What would you do differently if you were managing this queue?

Deliver a notebook or script, a `README.md` with your findings in plain language, and the SQL versions of your queries in `queries.sql`. Findings written for a manager, not for a programmer, are what get noticed.

## Done when

- [ ] You can load a CSV, inspect it (`head`, `info`, `describe`), and spot missing or odd values
- [ ] You can do `groupby`, `merge`, and date handling without looking up the syntax every time
- [ ] You can write a JOIN and a GROUP BY in SQL from memory
- [ ] You've called a public API with `requests` and handled errors and status codes
- [ ] The ticket analysis is pushed with a README that includes at least three charts
- [ ] You've used branches and PRs for this phase's work

## GitHub skill this phase

Part 3 of `docs/github-guide.md`: branches, PRs, issues. Do the whole phase on a feature branch and merge via a pull request.
