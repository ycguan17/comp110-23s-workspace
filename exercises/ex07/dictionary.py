"""Dictionary functions."""

__author__ : "730372605"


def invert(initial: dict[str, str]) -> dict[str, str]:
    new : dict[str, str] = {}
    for key in initial.keys():
        if initial[key] in new.keys():
            raise KeyError("Repeat keys/values")
        new[initial[key]] = key
    return new


def favorite_color(initial_dict: dict[str, str]) -> str:
    color : dict[str, str] = {}
    for item in initial_dict.keys():
        if color.has_key(initial_dict[item]):
            color[initial_dict[item]] += 1
        else:
            color[initial_dict[item]] = 1
    maxColor : str = color.keys()[0]
    for item in color.keys():
        if color[maxColor] < color[item]:
            maxColor = item
    return maxColor


def count(input: list[str]) -> dict[str, int]:
    newDic : dict[str, int] = {}
    for item in input:
        if item in newDic.keys:
            newDic[item] += 1
        else:
            newDic[item] = 1 
    return newDic