# Phase 1: Python Core, Testing, Git Basics (Weeks 1-2)

**Goal:** write small, correct Python programs without copying, and use Git daily.

## Topics

| Days | Topic | Practice |
|---|---|---|
| 1-2 | Variables, types, strings, f-strings, input/output, conditionals, loops | FizzBuzz, string clean-up |
| 3-4 | Lists, tuples, dicts, sets, comprehensions, sorting | Word counts, top-N |
| 5 | Functions, arguments, return values, scope, docstrings, type hints | Refactor earlier code into functions |
| 6-7 | Files, `pathlib`, JSON, CSV, `with` blocks | Read and write a JSON file |
| 8 | Errors and exceptions, `try/except`, raising `ValueError` | Validate input |
| 9-10 | Classes and objects, `__init__`, methods | `BankAccount` |
| 11 | Modules, imports, virtual environments, `pip`, `if __name__ == "__main__"` | Split code into files |
| 12 | Testing with pytest, reading a failing test | Make `test_exercises.py` pass |
| 13-14 | Mini project (below), cleanup, README, push | Log parser CLI |

## Exercises: the core of this phase

Open `exercises.py`. Every function raises `NotImplementedError` until you write it. Then run:

```bash
pytest phase-1-python -q
```

Work through them in order. Tests that fail are the point: read the failure, fix the code, run again. Commit after each function that turns green, for example `git commit -am "Implement fizzbuzz"`.

Rule: no AI assistant writing the solution for you. Use it to explain an error or a concept after you've tried. Typing the code yourself is how the skill sticks.

## Mini project: log parser CLI

Create `phase-1-python/log_parser.py`. Your program reads a log file where each line looks like:

```
2026-10-26 14:03 | ERROR | payment-service | timeout after 30s
```

and prints:

- count of lines per level (INFO, WARN, ERROR)
- the 3 services with the most errors
- every ERROR line from a given service, passed on the command line (`python log_parser.py app.log --service payment-service`)

Use your `parse_log_line` and `top_n` functions. Add a sample `sample.log`, a short README, and at least three tests of your own. Use `argparse` from the standard library for the command-line options.

This idea comes straight from support work, so you can describe it in interviews as a real tool.

## Done when

- [ ] All tests in `test_exercises.py` pass
- [ ] The log parser runs from the command line and has tests
- [ ] You've made at least 15 commits over two weeks, pushed to GitHub
- [ ] You can explain the difference between a list, a tuple, a set, and a dict, and when to use each
- [ ] You can read a Python traceback and point to the line that caused it
- [ ] Your virtual environment is set up and you know what it's for

## GitHub skill this phase

Part 1 and Part 2 of `docs/github-guide.md`. When the exercises pass, set up CI as in Part 5 if you like, or wait until Phase 5.
