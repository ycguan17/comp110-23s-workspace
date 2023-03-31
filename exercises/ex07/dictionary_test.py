"""Testing functions found in dictionary.py."""

__author__: "730372605"
from exercises.ex07.dictionary import invert, favorite_color, count

def test_letters() -> None:
    """Tests short dictionary of letters."""
    test_dictionary: dict[str, str] = {'a': 'z', 'b': 'y', 'c': 'x'}
    assert invert(test_dictionary) == {'z': 'a', 'y': 'b', 'x': 'c'}


def test_one_value() -> None: 
    """Tests dictionary with one value and key."""
    test_dictionary: dict[str, str] = {'apple': 'cat'}
    assert invert(test_dictionary) == {'cat': 'apple'}


def test_empty() -> None:
    """Tests dictionary with multiple values and keys and a empty key."""
    test_dictionary: dict[str, str] = {'horton': 'koury', 'manly': 'graham', 'craige': ''}
    assert invert(test_dictionary) == {'koury': 'horton', 'graham': 'manly', '': 'craige'}


def test_one_entry() -> None:
    """Gives most frequent color key with one entry in dictionary."""
    test_dictionary: dict[str, str] = {'Tyler': 'Yellow'}
    assert favorite_color(test_dictionary) == 'Yellow'


def test_multiple_entries() -> None:
    """Gives most frequent color key with multiple entries."""
    test_dictionary: dict[str, str] = {'Tyler': 'Yellow', 'Kevin': 'Blue', 'Anjani': 'Blue'}
    assert favorite_color(test_dictionary) == 'Blue'


def test_letter_values() -> None:
    """Instead of names, inputs letters before colors."""
    test_dictionary: dict[str, str] = {'T': 'Teal', 'G': 'Green', 'F': 'Green'}
    assert favorite_color(test_dictionary) == 'Green' 


def test_one_elem() -> None:
    """Given one element list, count keys."""
    test_list: list[str] = ["star"]
    assert count(test_list) == {"star":1}


def test_multiple_elem() -> None:
    """Given multiple elements in a list, count keys."""
    test_list: list[str] = ["star", "moon", "star", "druid", "moon"]
    assert count(test_list) == {"star": 2, "moon": 2, "druid": 1}


def test_greater_elem() -> None:
    """Given multiple elements in list, count keys."""
    test_list: list[str] = ["story", "story", "man", "grades", "story", "z"]
    assert count(test_list) == {"story": 3, "man": 1, "grades": 1, "z": 1}