"""Exercise 06: Dictionary Utils Unit Tests."""

__author__ = "730231193"

from exercises.ex06.dictionary import invert, count, favorite_color


def test_invert_empty() -> None:
    """Return empty dictionary if argument is empty."""
    test: dict[str, str] = dict()
    assert invert(test) == dict()


def test_invert_single_pair() -> None:
    """Invert one key-value pair if only one is present."""
    test: dict[str, str] = {'x': 'y'}
    assert invert(test) == {'y': 'x'}


def test_invert_multiple_pairs() -> None:
    """Use case test with multiple key-value pairs."""
    test: dict[str, str] = {'Naruto': 'Uzamaki', 'Izuku': 'Midoriya', 'Eren': 'Jaegar'}
    assert invert(test) == {'Uzamaki': 'Naruto', 'Midoriya': 'Izuku', 'Jaegar': 'Eren'}


def test_count_empty() -> None:
    """Return an empty dictionary if argument is empty."""
    test: list[str] = list()
    assert count(test) == dict()


def test_count_duplicates() -> None:
    """Functionality check for lists with unique values."""
    test: list[str] = ['MegaWeeb', "MegaWeeb", "MegaWeeb", "MegaWeeb"]
    assert count(test) == {'MegaWeeb': 4}


def test_count_mixed() -> None:
    """Use case check with duplicate / unique values."""
    test: list[str] = ['Pikachu', 'Charmander', 'Charizard', 'Charizard', 'Pikachu', 'Bulbasaur']
    assert count(test) == {'Pikachu': 2, 'Charmander': 1, 'Charizard': 2, 'Bulbasaur': 1}


def test_favorite_color_empty() -> None: 
    """Return message if empty dictionary passed."""
    test: dict[str, str] = dict()
    assert favorite_color(test) == 'The dictionary is empty.'


def test_favorite_color_four_way_tie() -> None:
    """Return value that occurred first in case of tie."""
    test: dict[str, str] = {'Goku': 'blue', 'Vegeta': 'yellow', 'Piccolo': 'green', 'Freiza': 'red'}
    assert favorite_color(test) == 'blue'


def test_favorite_color_one_winner() -> None:
    """Use case test with one definitive winner."""
    test: dict[str, str] = {'Ricky': 'blue', 'Julian': 'yellow', 'Bubbles': 'blue', 'Randy': 'yellow', 'Lahey': 'blue'}
    assert favorite_color(test) == 'blue'
