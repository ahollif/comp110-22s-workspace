"""Some examples of tender, loving function definitions."""


def tender_love(name: str) -> str:
    """Given a name as a parameter, returns a loving string."""
    return f"I love you {name}, can I have your babies?"


def spread_love(to: str, n: int) -> str:
    """Generates a string that repeats a loving message n times."""
    love_note = ""
    i = 0
    while i < n:
        love_note += f"{tender_love(to)}\n"
        i += 1
    return love_note