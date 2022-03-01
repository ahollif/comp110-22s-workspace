"""Tests for the sum function."""

from lessons.sum import sum


def test_empty_sum() -> None:
    xs: list[float] = []
    assert sum(xs) == 0.0


def test_single_sum_item() -> None:
    xs: list[float] = [420.0]
    assert sum(xs) == 420.0


def test_many_items() -> None:
    xs: list[float] = [111, 222, 444]
    assert sum(xs) == 777.0


def test_many_items_again() -> None:
    assert sum([-1.0, 1.0, -2.0, 2.0]) == 0.0
