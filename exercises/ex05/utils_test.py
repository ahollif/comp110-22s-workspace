"""Exercise 05: Unit testing for list toolkit."""

__author__ = "730231193"

from exercises.ex05.utils import only_evens, sub, concat


def test_only_evens_empty() -> None:
    """Return an empty list if list input is blank."""
    xs: list[int] = list()
    assert only_evens(xs) == []


def test_only_evens_evens() -> None:
    """Return full list if list only contains even numbers."""
    xs: list[int] = [2, 4, 6]
    assert only_evens(xs) == [2, 4, 6]


def test_only_evens_mixed() -> None:
    """Return only even numbers when list contains positive and negative ints."""
    xs: list[int] = [1, 3, 4, 7, 8]
    assert only_evens(xs) == [4, 8]


def test_only_evens_mixed_again() -> None:
    """Another use case test."""
    xs: list[int] = [2, 3, 4, 66, 78, 99, 100]
    assert only_evens(xs) == [2, 4, 66, 78, 100]


def test_sub_empty_list() -> None:
    """Return an empty list when list is blank."""
    xs: list[int] = list()
    assert sub(xs, 1, 3) == []


def test_sub_one_item() -> None:
    """Return only the first index when len of list == 1."""
    xs: list[int] = [1]
    assert sub(xs, 0, 3) == [1]


def test_sub_invalid_max() -> None: 
    """Return an empty list if max is negative."""
    xs: list[int] = [10, 20, 30, 40]
    assert sub(xs, 1, -4) == []


def test_sub_invalid_min() -> None:
    """Return an empty list if min > length of list."""
    xs: list[int] = [10, 20, 30]
    assert sub(xs, 6, 0) == []


def test_sub_multiple_items() -> None:
    """Return only values within index positions passed as arguments."""
    xs: list[int] = [10, 20, 30, 40]
    assert sub(xs, 1, 3) == [20, 30]


def test_sub_multiple_items_again() -> None:
    """Another use case test."""
    xs: list[int] = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
    assert sub(xs, 2, 8) == [30, 40, 50, 60, 70, 80]


def test_concat_two_empty() -> None:
    """Return an empty list if both arguments are blank lists."""
    xs: list[int] = list()
    ys: list[int] = list()
    assert concat(xs, ys) == list()


def test_concat_empty_xs() -> None:
    """Return only one list if one argument is a blank list."""
    xs: list[int] = list()
    ys: list[int] = [40, 50, 60]
    assert concat(xs, ys) == [40, 50, 60]


def test_concat_full_lists() -> None:
    """Return concatenated version of both lists."""
    xs: list[int] = [10, 20, 30]
    ys: list[int] = [40, 50, 60]
    assert concat(xs, ys) == [10, 20, 30, 40, 50, 60]


def test_concat_full_lists_again() -> None:
    """Another use case test."""
    xs: list[int] = list(range(1, 9))
    ys: list[int] = list(range(9, 20))
    assert concat(xs, ys) == list(range(1, 20))