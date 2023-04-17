"""Functions for data wrangling."""

__author__ : "730372605"

from csv import DictReader

def read_csv_rows(filename: str) -> list[dict[str,str]]: 
    """Read csv file and return a list of dictionaries"""
    result: list[dict[str,str]] = []
    file_handle = open(filename, "r", encoding = "utf8")
    csv_reader = DictReader(file_handle)
    for row in csv_reader:
        result.append(row)
    file_handle.close()

    return result

def column_values(table: list[dict[str,str]], header: str) -> list[str]:
    """Returns values on a table under a certain header"""
    result: list[str] = []
    #step through table
    for row in table:
        #save every value under key "header"
        result.append(row[header])

    return result

def columnar(table: list[dict[str,str]]) -> dict[str, list[str]]:
    """Reformats data so that it's a dictionary with column headers as keys"""
    result: dict[str, list[str]] = {}
    #loop through keys of one row of table
    first_row: dict[str,str] = table[0]
    for key in first_row:
        #for each key, make a disctionary entry with all column values
        result[key] = column_values(table, key)

    return result

def head(table: dict[str, list[str]], rows: int) -> dict[str, list[str]]:
    result: dict[str, list[str]] = {}
    for key in table:
        values: list[str] = []
        length: int = rows
        if rows > len(table[key]):
            length = len(table[key])
        for i in range(length):
            values.append(table[key][i])
        result[key] = values

    return result

def select(table: dict[str, list[str]], column: list[str]) -> dict[str, list[str]]:
    result: dict[str, list[str]] = {}
    idx: int = 1
    for col in column:
        values: list[str] = []
        for elem in table[col]:
            values.append(elem)
        result[col] = values

    return result

def concat(table1: dict[str, list[str]], table2: dict[str, list[str]]) -> dict[str, list[str]]:
    result: dict[str, list[str]] = {}
    for tab in table1:
        result[tab] = table1[tab]

    for tab in table2:
        if tab in result:
            result[tab] += table2[tab]
        else:
            result[tab] = table2[tab]

    return result

def count(values: list[str]) -> dict[str, int]:
    result: dict[str, int] = {}
    for elem in values:
        if elem in result:
            result[elem] += 1
        else:
            result[elem] = 1
    
    return result