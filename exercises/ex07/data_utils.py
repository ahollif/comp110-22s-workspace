"""Dictionary related utility functions."""

__author__ = "730231193"

# Define your functions below

from csv import DictReader


def read_csv_rows(filename: str) -> list[dict[str, str]]:
    """Read the rows of a csv into a 'table'."""
    result: list[dict[str, str]] = []

    # Open a handle to the data file
    file_handle = open(filename, "r", encoding="utf8")

    # Prepare to read the data file as a CSV rather than just strings
    csv_reader = DictReader(file_handle)

    # Read each row of the CSV file line-by-line
    for row in csv_reader:
        result.append(row)

    # Close the file when done to free its resources
    file_handle.close()

    return result


def column_values(table: list[dict[str, str]], column: str) -> list[str]:
    """Produce a list[str] of all values in a single column."""
    result: list[str] = []
    for row in table:
        item: str = row[column]
        result.append(item)
    return result


def columnar(row_table: list[dict[str, str]]) -> dict[str, list[str]]:
    """Transform a row-oriented table to a column-oriented table."""
    result: dict[str, list[str]] = {}

    first_row: dict[str, str] = row_table[0]
    for column in first_row:
        result[column] = column_values(row_table, column)

    return result


def head(column_table: dict[str, list[str]], n: int) -> dict[str, list[str]]:
    """Returns a column-table with only parameter n first rows visible."""
    result: dict[str, list[str]] = {}
    for column in column_table:
        new_list: list[str] = []
        result[column] = new_list
        for i in range(0, n):
            new_list.append(column_table[column][i])
    return result


def select(column_table: dict[str, list[str]], names: list[str]) -> dict[str, list[str]]:
    """Returns first 10 rows of selected column names."""
    result: dict[str, list[str]] = {}
    for item in names:
        result[item] = column_table[item]
    return result


def concat(c_table1: dict[str, list[str]], c_table2: dict[str, list[str]]) -> dict[str, list[str]]:
    result: dict[str, list[str]] = {}
    for key in c_table1: 
        result[key] = c_table1[key]
    for key in c_table2:
        if key in result:
            for i in range(0, len(c_table2[key])):
                result[key].append(c_table2[key][i])
        else:
            result[key] = c_table2[key]    
    return result


def count(column: list[str]) -> dict[str, int]:
    "Returns unique values from lists with their counts in a dict."
    result: dict[str, int] = {}
    for item in column:
        if item not in result:
            result[item] = 1
        else:
            result[item] += 1
    return result
    