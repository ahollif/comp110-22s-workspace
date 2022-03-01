"""Examples of using lists in a simple 'game'."""

from random import randint

rolls: list[int] = list()

while len(rolls) == 0 or rolls[-1] != 1:
    rolls.append(randint(1, 6))

print(rolls)