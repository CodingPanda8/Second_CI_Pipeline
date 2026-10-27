
import importlib

module = importlib.import_module("35_move_zeros")


def test_move_zeros_to_end():
    assert module.move_zeros([0, 1, 0, 3, 12]) == [1, 3, 12, 0, 0]


def test_list_without_zeros():
    assert module.move_zeros([1, 2, 3]) == [1, 2, 3]


def test_all_zeros_and_empty_list():
    assert module.move_zeros([0, 0]) == [0, 0]
    assert module.move_zeros([]) == []