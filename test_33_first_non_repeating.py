
import importlib

module = importlib.import_module("33_first_non_repeating")


def test_first_non_repeating_character():
    assert module.first_non_repeating("aabbcdd") == "c"


def test_first_unique_character():
    assert module.first_non_repeating("abcab") == "c"


def test_no_non_repeating_character():
    assert module.first_non_repeating("aabb") is None