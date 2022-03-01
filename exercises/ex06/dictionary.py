"""Exercise 06: Dictionary Utils."""

__author__ = "730231193"


def invert(dictionary: dict[str, str]) -> dict[str, str]:
    """Inverts key-value pairs in a dictionary."""
    if dictionary == dict():
        return dict()
    result: dict[str, str] = dict()
    for key in dictionary:
        if dictionary[key] not in result:
            result[dictionary[key]] = key
        else:
            raise KeyError
    return result


def count(strings: list[str]) -> dict[str, int]:
    """Returns dictionary mapping with counts of how many instances a string is present in a list."""
    if strings == dict():
        return dict()
    result: dict[str, int] = dict()
    for item in strings:
        if item not in result:
            result[item] = 1
        else: 
            result[item] += 1
    return result


def favorite_color(colors: dict[str, str]) -> str:
    """Finds color (or more generally, string value) most common in a dictionary."""
    if colors == dict(): 
        return 'The dictionary is empty.'
    key_list: list[str] = list()
    for key in colors:
        key_list.append(colors[key])
    dictionary_count: dict[str, int] = count(key_list)
    maximum: int = 0
    result: str = ""
    for key in dictionary_count: 
        if dictionary_count[key] > maximum:
            maximum = dictionary_count[key]
            result = key
    return result
