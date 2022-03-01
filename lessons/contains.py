"""Function that determines if a list contains an item."""

__name__ = "Adam_Is_The_Best"


def contains(needle: str, haystack: list[str]) -> bool:
    i: int = 0
    while i < len(haystack):
        if haystack[i] == needle:
            return True
        else:
            i += 1
    return False


def contains_for(needle: str, haystack: list[str]) -> bool:
    for item in haystack:
        if item == needle:
            return True
    return False


def contains_less_code(needle: str, haystack: list[str]) -> bool:
    if needle in haystack:
        return True
    else:
        return False


def Adam_Is_The_Best() -> None:
    guess = input("Pick a word... ")
    acceptable_choices: list[str] = ["pokemon", "digimon"]
    if contains(guess, acceptable_choices):
        print("We're letting you in the secret club")
    else:
        print("Go back to Davis")


if __name__ == "__Adam_Is_The_Best__":
    Adam_Is_The_Best()