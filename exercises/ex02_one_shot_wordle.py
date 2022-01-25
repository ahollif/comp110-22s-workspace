"""Exercise 2: One Shot Wordle."""

__author__ = "730231193"

secret_word = "python"
word_length = len(secret_word)

guess = input(f"What is your {word_length}-letter guess? ")
input_test = True


# Variable input_test is a bool initialized as True
# Redefines as False to terminate while loop below once guess of correct length is made
# Also redefines variable guess once given input of correct length
while input_test:
    if len(guess) == word_length:
        input_test = False
    else: 
        guess = input(f"That was not {word_length} letters! Try again: ")


WHITE_BOX = "\U00002B1C"
GREEN_BOX = "\U0001F7E9"
YELLOW_BOX = "\U0001F7E8"

i = 0  # Counter for main while loop below used for index checks and eventual loop termination
output_string = ""  # Blank string that will be appended using constants above ^^ and eventually printed as output

while i < word_length:
    if guess[i] == secret_word[i]:
        output_string += GREEN_BOX
    else: 
        yellow_counter = 0
        yellow_test = True

        # While loop below keeps indexed character of the guess constant while
        # Looping through and checking for matches with each character instance of secret word
        while yellow_counter < word_length and yellow_test:
            if guess[i] == secret_word[yellow_counter]:
                yellow_test = False
            else: 
                yellow_counter += 1

        # If matching characters are found at some point between the two variables, append a yellow box
        # Otherwise, append a white box
        if not(yellow_test):
            output_string += YELLOW_BOX
        else:
            output_string += WHITE_BOX

    # Add one to the primary counter variable to continue iterating
    i += 1

print(output_string)

if guess == secret_word:
    print("Woo! You got it!")
else: 
    print("Not quite. Play again soon!")