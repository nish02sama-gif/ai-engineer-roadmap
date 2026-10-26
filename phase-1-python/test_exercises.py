import json

import pytest

from exercises import (
    BankAccount,
    fizzbuzz,
    flatten,
    is_palindrome,
    parse_log_line,
    read_json_file,
    top_n,
    word_count,
)


def test_fizzbuzz():
    assert fizzbuzz(5) == ["1", "2", "Fizz", "4", "Buzz"]
    assert fizzbuzz(15)[-1] == "FizzBuzz"
    assert fizzbuzz(0) == []


def test_word_count():
    assert word_count("Hello, hello world!") == {"hello": 2, "world": 1}
    assert word_count("") == {}


def test_is_palindrome():
    assert is_palindrome("A man, a plan, a canal: Panama")
    assert is_palindrome("")
    assert not is_palindrome("hello")


def test_flatten():
    assert flatten([1, [2, [3, 4]], 5]) == [1, 2, 3, 4, 5]
    assert flatten([]) == []
    assert flatten([[], [[]]]) == []


def test_top_n():
    assert top_n({"a": 3, "b": 5, "c": 3}, 2) == [("b", 5), ("a", 3)]
    assert top_n({}, 3) == []
    assert top_n({"x": 1}, 5) == [("x", 1)]


def test_read_json_file(tmp_path):
    good = tmp_path / "good.json"
    good.write_text(json.dumps({"a": 1}))
    assert read_json_file(good) == {"a": 1}

    assert read_json_file(tmp_path / "missing.json") == {}

    bad = tmp_path / "bad.json"
    bad.write_text("{not json")
    with pytest.raises(ValueError):
        read_json_file(bad)


def test_bank_account():
    acct = BankAccount(100)
    acct.deposit(50)
    acct.withdraw(30)
    assert acct.balance == 120
    assert BankAccount().balance == 0


def test_bank_account_errors():
    acct = BankAccount(10)
    with pytest.raises(ValueError):
        acct.withdraw(11)
    with pytest.raises(ValueError):
        acct.deposit(0)
    with pytest.raises(ValueError):
        acct.withdraw(-5)
    assert acct.balance == 10


def test_parse_log_line():
    line = "2026-10-26 14:03 | ERROR | payment-service | timeout after 30s"
    assert parse_log_line(line) == {
        "timestamp": "2026-10-26 14:03",
        "level": "ERROR",
        "service": "payment-service",
        "message": "timeout after 30s",
    }
    with pytest.raises(ValueError):
        parse_log_line("not a valid line")
