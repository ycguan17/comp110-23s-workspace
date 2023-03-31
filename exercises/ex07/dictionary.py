"""Dictionary functions."""

__author__: "730372605"


def invert(initial: dict[str, str]) -> dict[str, str]:
    """Flips values and keys within dictionary."""
    new: dict[str, str] = {}
    for key in initial.keys():
        if initial[key] in new.keys():
            raise KeyError("Repeat keys/values")
        new[initial[key]] = key
    return new


def favorite_color(initial: dict[str, str]) -> str:
    """Finds the most frequent key in dictionary."""
    color: dict[str, str] = {}
    for item in initial.keys():
        if initial[item] in color.keys():
            color[initial[item]] += 1
        else:
            color[initial[item]] = 1
    maxColor: str = color.keys()[0]
    for item in color.keys():
        if color[maxColor] < color[item]:
            maxColor = item
    return maxColor


def count(input: list[str]) -> dict[str, int]:
    """Count the unique elements of the list into a dictionary."""
    newDic: dict[str, int] = {}
    for item in input:
        if item in newDic.keys:
            newDic[item] += 1
        else:
            newDic[item] = 1 
    return newDic