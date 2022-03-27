"""Generates a random password of desired length."""

from random import randint

potential_chars: list[str] = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '!', '@', '#', '$', '%', '^', '&', '*']


def integer_input() -> int:
    """Prompts the user for input."""
    valid: bool = False
    output: str = input('Please input desired password length as an integer: ')
    while not valid:
        if not output.isnumeric():
            output = input('Try again -- please input desired length as an integer: ')
        else: 
            valid = True
    return int(output)


def main() -> None:
    length: int = integer_input()
    password: str = ""
    for i in range(0, length):
        character: str = potential_chars[randint(0, len(potential_chars) - 1)]
        if character.isalpha():
            capital: int = randint(0, 1)
            if capital:
                password += character.capitalize()
            else:
                password += character
        else: 
            password += character
    print(password)


if __name__ == "__main__":
    main()