"""An example of a while loop."""

counter: int = 0
maximum: int = int(input("Count up to, but not including what? "))

while counter < maximum:  # Repeat block follows

    # Repeat block below only evaluates if condition above is True

    counter_squared = counter ** 2
    print("The square of " + str(counter) + " is " + str(counter_squared))
    counter += 1  # Progress must be made toward condition becoming false

print("Done!")