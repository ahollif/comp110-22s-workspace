"""Exercise 05: List function toolkit."""

__author__ = "730231193"


def only_evens(xs: list[int]) -> list:
    """Returns only even integers from a list."""
    output: list[int] = list()
    for numbers in xs:
        if numbers % 2 == 0:
            output.append(numbers)
    return output


def sub(xs: list[int], min: int, max: int) -> list[int]:
    """Returns list items beginning at index pos min (inclusive) and ending at index pos max (exclusive)."""
    if len(xs) == 0:
        return xs
    if min > len(xs):
        return list()
    if max <= 0:
        return list()
    if min < 0:
        min = 0
    if max > len(xs): 
        max = len(xs)
    i: int = min
    output: list[int] = list()
    while i < max:
        output.append(xs[i])
        i += 1
    return output
    

def concat(xs: list[int], ys: list[int]) -> list[int]:
    """Concatenates two list arguments and returns as one."""
    output: list[int] = list()
    if len(xs) > 0:
        i: int = 0
        while i < len(xs):
            output.append(xs[i])
            i += 1
    if len(ys) > 0:
        i: int = 0
        while i < len(ys):
            output.append(ys[i])
            i += 1
    return output 
    