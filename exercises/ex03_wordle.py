"""Exercise 03: Structured Wordle."""

from random import randint

__author__ = "730231193"

WHITE_BOX = "\U00002B1C"
GREEN_BOX = "\U0001F7E9"
YELLOW_BOX = "\U0001F7E8"


def contains_char(string: str, char: str) -> bool:
    """Checks to see if a string contains an instance of a specified character."""
    assert len(char) == 1  # Assume char variable is a string of length 1 (i.e., a single character)
    i = 0
    while i < len(string):  # Loops through string to check if it contains char, returns True / False
        if string[i] == char:
            return True  # Terminate function once a match is found
        else: 
            i += 1
    return False  # If match isn't found and while loop terminates, return False


def emojified(guess: str, secret: str) -> str:
    """Returns an emojified output string that indicates appropriate character sequence of guess with respect to the secret."""
    assert len(secret) == len(guess)  # Assume lengths of character and guess are equal
    i = 0  # Iterator that allows for looping through each character index of the variable guess
    output_string = ""
    while i < len(secret):
        if guess[i] == secret[i]:  # In case of exact match, append a green box
            output_string += GREEN_BOX
            i += 1
        elif contains_char(secret, guess[i]):  # If secret at least contains character instance, append a yellow box
            output_string += YELLOW_BOX
            i += 1
        else:  # Otherwise, append a white box
            output_string += WHITE_BOX
            i += 1
    return output_string


def input_guess(number: int) -> str:
    """Prompts the user for an input given expected string length."""
    guess = input(f"Enter a {number} character word: ")
    while len(guess) != number:  # Utilize while loop to prompt user for input until length is appropriate
        guess = input(f"That wasn't {number} chars! Try again: ")
    return guess  # Function returns user's input as a string


def main() -> None:
    """The entrypoint of the program and main game loop."""
    turn = 1  # Used as a turn counter and also for eventual termination of the while loop below
    possible_words: list[str] = ["point", "house", "codes", "mommy", "chest", "drape"]
    SECRET = possible_words[randint(0, (len(possible_words) - 1))]
    while turn <= 6:
        print(f"==Turn {turn}/6==")
        guess = input_guess(len(SECRET))  # Prompts the user for a guess using previously defined input_guess func and len of secret word
        print(emojified(guess, SECRET))  # Prints emoji output using previously defined emojified func, secret word, and the guess variable
        if guess == SECRET:  # In case of correct guess, terminate the function
            print(f"You won in {turn}/6 turns!")
            return  # return statement will terminate the function
        else:  # Otherwise, increase turn var by 1 and begin game loop again
            turn += 1
    print("X/6 - You suck!")  # Notify the user they have lost if while loop terminates before correct guess is made
    return  # Terminates the function


if __name__ == "__main__":
    main()
