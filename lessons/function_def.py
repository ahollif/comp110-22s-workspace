"""An example of function definiton."""


def my_max(a: int, b: int) -> int:
    """Returns the largest argument."""
    if a >= b: 
        return a
    else: 
        return b


x = 6
y = 7
z = my_max(x, y)
print(z)