"""Prisoner's Dilemma Game."""


def choice() -> str:
    """Prompts user for input."""
    acceptable_choices: list[str] = ["Silence", "Confession"]
    choice = input("Choose either 'Silence' or 'Confession': ").capitalize()
    while choice not in acceptable_choices:
        choice = input("You dumbass! Choose either 'Silence' or 'Confession': ").capitalize()
    return choice


def computer_choice() -> str:
    player_choice = choice()
