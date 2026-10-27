
import importlib

module = importlib.import_module("37_rotate_string")


def test_rotate_right_by_two():
    assert module.rotate_string("abcdef", 2) == "efabcd"


def test_rotation_larger_than_string_length():
    assert module.rotate_string("abc", 4) == "cab"


def test_empty_string_and_zero_rotation():
    assert module.rotate_string("", 3) == ""
    assert module.rotate_string("abc", 0) == "abc"
