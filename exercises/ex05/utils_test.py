from exercises.ex05.utils import only_evens, sub, concat

"""Unit tests for ex05 utility functions."""

__author__: "730372605"


def test_one_elem() -> None:
    """Tests one element list for only_evens."""
    test_list: list[int] = [4]
    assert only_evens(test_list) == [4]


def test_many_elems() -> None:
    """Tests many element list for only_evens."""
    test_list: list[int] = [4, 3, 1, 6, 8]
    assert only_evens(test_list) == [4, 6, 8]


def test_many_with_negative_elems() -> None:
    """Tests many element list with negatives for only_evens."""
    test_list: list[int] = [4, -3, 1, -6, 8]
    assert only_evens(test_list) == [4, -6, 8]


def test_only_one_element() -> None:
    """Tests one element list for sub."""
    test_list: list[int] = [4]
    test_idx1: int = 1
    test_idx2: int = 3
    assert sub(test_list, test_idx1, test_idx2) == []


def test_many_elements() -> None:
    """Tests many elements in list for sub."""
    test_list: list[int] = [4, 2, 5, 3]
    test_idx1: int = 1
    test_idx2: int = 3
    assert sub(test_list, test_idx1, test_idx2) == [2, 5]


def test_many_with_negative_elements() -> None:
    """Tests many elements in list with negatives for sub."""
    test_list: list[int] = [3, 45, -1, 20, 4]
    test_idx1: int = -2
    test_idx2: int = 5
    assert sub(test_list, test_idx1, test_idx2) == [3, 45, -1, 20, 4]


def test_one_element() -> None:
    """Tests one element lists for concat."""
    test_list1: list[int] = [4]
    test_list2: list[int] = [3]
    assert concat(test_list1, test_list2) == [4, 3]


def test_many() -> None:
    """Tests many element lists for concat."""
    test_list1: list[int] = [1, 2, 3]
    test_list2: list[int] = [3, 1, 5]
    assert concat(test_list1, test_list2) == [1, 2, 3, 3, 1, 5]


def test_many_with_negatives() -> None:
    """Tests many element lists with negative numbers for concat."""
    test_list1: list[int] = [1, -2, 3]
    test_list2: list[int] = [-3, 1, 5]
    assert concat(test_list1, test_list2) == [1, -2, 3, -3, 1, 5]
