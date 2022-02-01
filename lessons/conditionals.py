"""An example of conditionals (if-else) statements."""

from random import choice
SECRET = choice(list(range(1, 6)))
test = True


while test is True:
    guess = int(input('Pick a number 1-5: '))

    if guess != SECRET:
        if guess == SECRET - 1 or guess == SECRET + 1:
            print('Close! Try adding or subtracting one.')
        else:
            print("You're way off there bud.")

    else:
        print('Correct!!!')
        test = False