"""List Utility Functions."""

__author__: "730372605"


def all(intList: list[int], num: int) -> bool:
    """Given a list of ints and a int, returns bool for if the list and int are the same."""
    idx: int = 0
    while idx < len(intList):
        if num != intList[idx]:
            return False
        idx += 1
    return True

def max(intList : list[int]) -> int:
    """Returns the largest in the List."""
    if len(intList) == 0:
        raise ValueError("max() arg is an empty List")
    idx: int = 0
    maxNum: int = intList[idx]
    while idx < len(intList):
        if maxNum < intList[idx]:
            maxNum = intList[idx]
        idx += 1
    return maxNum

def is_equal(list1: list[int], list2: list[int]) -> bool:
    """Returns True if every element at every index is equal in both list1 and list2."""
    idx: int = 0
    if len(list1) != len(list2):
        return False
    while idx < len(list1) and idx < len(list2):
        if list1[idx] != list2[idx]:
            return False
        idx += 1
    return True

def test() -> None:
    print("----Testing ALL function----")
    print(all([1, 2, 3], 1))
    print(all([1, 1, 1], 2))
    print(all([1, 1, 1], 1))

    print("----Testing MAX function----")
    print(max([1, 3, 2]))
    print(max([100, 99, 98]))
    #print(max([]))

    print("----Testing IS_EQUAL function----")
    print(is_equal( [1, 0, 1], [1, 0, 1]))
    print(is_equal( [1, 0, 1], [1, 0, 1]))

