"""New Function utilities with lists."""

__author__: "730372605"


def only_evens(old_list: list[int]) -> list[int]:
    """Given a list returns a new list where the elements are only even."""
    even_list: list[int] = []
    for elem in old_list:
        if elem % 2 == 0:
            even_list.append(elem)
    return even_list


def concat(list1: list[int], list2: list[int]) -> list[int]:
    """Given two lists, combines both lists in order."""
    new_list: list[int] = []
    for elem in list1:
        new_list.append(elem) 
    for elem in list2:
        new_list.append(elem)
    return new_list


def sub(numlist: list[int], start_idx: int, end_idx: int) -> list[int]:
    """Makes a subset list starting from start index ending at 1- end index."""
    end_list: list[int] = []
    if start_idx < 0:
        start_idx = 0
    if end_idx > len(numlist):
        end_idx = len(numlist)
    if len(numlist) == 0 or start_idx >= len(numlist) or end_idx <= 0:
        return end_list
    else:
        for idx in range(start_idx, end_idx):
            end_list.append(numlist[idx])
        return end_list