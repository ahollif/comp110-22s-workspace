"""EX01 - Chardle - A cute step toward Wordle."""

__author__ = "730231193"

magic_word: str = input("Enter a 5-character word: ")

if len(magic_word) != 5:
    print("Error: Word must contain 5 characters.")
    exit()
else: 
    magic_word = magic_word.lower()

magic_character: str = input("Enter a single character: ")

if len(magic_character) != 1:
    print("Error: Character must be a single character.")
    exit()
else: 
    magic_character = magic_character.lower()

# I have some Python background, so I know it'll be more efficient to use a for loop for the next step.
# However, I understand the same thing could be accomplished using a series of if statements. 

print("\n" + "Searching for " + magic_character + " in " + magic_word + "\n")

ticker = 0  # Increasing ticker that allows for iteration through magic word
instances = 0  # Running counter for instances of magic character

for char in magic_word:
    if magic_word[ticker] == magic_character:
        print(magic_character + " found at index " + str(ticker))
        ticker += 1 
        instances += 1
    else:
        ticker += 1  # Index position checked will increase regardless of magic character being found or not

if instances > 0:
    print("\n" + str(instances) + " instance of " + magic_character + " found in " + magic_word)
else:
    print("\n" + "No instances of " + magic_character + " found in " + magic_word)