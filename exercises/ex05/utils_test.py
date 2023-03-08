"""Unit tests for ex05 utility functions"""

__author__: "730372605"

from exercises.ex05.utils import only_evens, sub, concat

def test_one_element() -> None:
    test_list: list[int] = [4]
    assert only_evens(test_list) == [4]

def test_many() -> None:
    test_list1: list[int] = [1, 2, 3]
    test_list2: list[int] = [3, 1, 5]
    assert concat(test_list1, test_list2) == [1, 2, 3, 3, 1, 5]

def test_many_with_negatives() -> None:
    test_list: list[int] = [3, 45, 1, 20, 4]
    test_idx1: int = -2
    test_idx2: int = 5
    assert sub(test_list, test_idx1, test_idx2) == [3, 45, 1, 20, 4]