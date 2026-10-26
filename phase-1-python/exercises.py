"""Phase 1 exercises. Replace each `raise NotImplementedError` with working code.

Run the tests with:  pytest phase-1-python -q
Work in order. Commit after each function that passes.
"""
import json
import re
from pathlib import Path


def fizzbuzz(n: int) -> list[str]:
    """Return a list for numbers 1..n.

    Multiples of 3 -> "Fizz", multiples of 5 -> "Buzz", multiples of both -> "FizzBuzz",
    otherwise the number as a string.
    fizzbuzz(5) -> ["1", "2", "Fizz", "4", "Buzz"]
    """
    result = []

    for i in range(1, n + 1):
        if i%3==0 and i%5==0:
            result.append("FizzBuzz")
        elif i%3==0:
            result.append("Fizz")
        elif i%5==0:
            result.append("Buzz")
        else:
            result.append(str(i))

    return result
    


def word_count(text: str) -> dict[str, int]:
    """Count how often each word appears. Ignore case and punctuation.

    word_count("Hello, hello world!") -> {"hello": 2, "world": 1}
    Hint: re.findall(r"[a-z']+", text.lower())
    """
    raise NotImplementedError


def is_palindrome(s: str) -> bool:
    """True if s reads the same forwards and backwards, ignoring case and any
    character that is not a letter or digit.

    is_palindrome("A man, a plan, a canal: Panama") -> True
    """
    raise NotImplementedError


def flatten(nested: list) -> list:
    """Flatten a list of any depth into a single flat list.

    flatten([1, [2, [3, 4]], 5]) -> [1, 2, 3, 4, 5]
    Hint: recursion, and isinstance(item, list).
    """
    raise NotImplementedError


def top_n(counts: dict[str, int], n: int) -> list[tuple[str, int]]:
    """Return the n items with the highest counts as (key, count) tuples.

    Sort by count descending; break ties alphabetically by key.
    top_n({"a": 3, "b": 5, "c": 3}, 2) -> [("b", 5), ("a", 3)]
    """
    raise NotImplementedError


def read_json_file(path: str | Path) -> dict:
    """Read a JSON file and return its contents as a dict.

    If the file doesn't exist, return an empty dict.
    If the file isn't valid JSON, raise ValueError with a clear message.
    """
    raise NotImplementedError


class BankAccount:
    """A simple account.

    - starts at balance 0 (or a given opening balance)
    - deposit(amount): amount must be > 0, otherwise raise ValueError
    - withdraw(amount): amount must be > 0 and <= balance, otherwise raise ValueError
    - balance is available as the attribute `balance`
    """

    def __init__(self, opening_balance: float = 0) -> None:
        raise NotImplementedError

    def deposit(self, amount: float) -> None:
        raise NotImplementedError

    def withdraw(self, amount: float) -> None:
        raise NotImplementedError


def parse_log_line(line: str) -> dict[str, str]:
    """Parse a log line of the form:

    "2026-10-26 14:03 | ERROR | payment-service | timeout after 30s"

    into {"timestamp": "2026-10-26 14:03", "level": "ERROR",
          "service": "payment-service", "message": "timeout after 30s"}

    Raise ValueError if the line does not have exactly 4 fields separated by " | ".
    """
    raise NotImplementedError
