"""Exercise 2: One Shot Wordle."""

__author__ = "730231193"

WHITE_BOX = "\U00002B1C"
GREEN_BOX = "\U0001F7E9"
YELLOW_BOX = "\U0001F7E8"

secret_word = "python"
word_length = len(secret_word)

guess = input(f"What is your {word_length}-letter guess? ")
input_test = True


# Variable input_test is a bool initialized as True
# Redefines as False to terminate while loop below once guess of correct length is made
# Loop redefines variable {guess} once given input of correct length
while input_test:
    if len(guess) == word_length:
        input_test = False
    else: 
        guess = input(f"That was not {word_length} letters! Try again: ")

i = 0 
output_string = ""

while i < word_length:
    if guess[i] == secret_word[i]:
        output_string += GREEN_BOX
    else:
        yellow_check = False
        yellow_ticker = 0
        for char in secret_word:
            if guess[i] == secret_word[yellow_ticker]:
                yellow_check = True
                yellow_ticker += 1
            else:
                yellow_ticker += 1
        if yellow_check:
            output_string += YELLOW_BOX
        else:
            output_string += WHITE_BOX
    i += 1

print(output_string)

if guess == secret_word:
    print("Woo! You got it!")
else: 
    print("Not quite. Play again soon!")
    
