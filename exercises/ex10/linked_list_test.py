"""Tests for linked list utils."""


from exercises.ex10.linked_list import Node, last, value_at, max, linkify, is_equal, scale
import pytest

__author__ = "730231193"


def test_last_empty() -> None:
    """Last of an empty Linked List should raise an value error."""
    with pytest.raises(ValueError):
        last(None)


def test_last_non_empty() -> None:
    """Last of a non-empty list should return a reference to its last Node."""
    linked_list = Node(0, Node(1, Node(2, None)))
    assert last(linked_list) == 2


def test_last_non_empty_v2() -> None:
    """Another use-case test that should return a reference to the last Node."""
    linked_list = Node(0, Node(1, Node(2, Node(3, None))))
    assert last(linked_list) == 3


def test_value_at_empty() -> None:
    """Empty Linked List should return an index error."""
    with pytest.raises(IndexError):
        value_at(None)


def test_value_at_non_empty_index_zero() -> None:
    """Function should return a reference to its first node given default parameter of 0."""
    linked_list = Node(0, Node(1, Node(2, Node(3, None))))
    assert value_at(linked_list) == 0


def test_value_at_non_empty_index_two() -> None:
    """Function should return a reference to its third node given an index argument of 2."""
    linked_list = Node(0, Node(1, Node(2, Node(3, None))))
    assert value_at(linked_list, 2) == 2


def test_value_at_non_empty_index_out_of_bounds() -> None:
    """Function should raise an index error if the index argument is out of bounds."""
    linked_list = Node(0, Node(1, Node(2, Node(3, None))))
    with pytest.raises(IndexError):
        value_at(linked_list, 4)


def test_max_empty_list() -> None:
    """Max of an empty linked list should raise a value error."""
    with pytest.raises(ValueError):
        max(None)


def test_max_non_empty_ordered() -> None:
    """Max of an ordered linked list should return the maximum value."""
    linked_list = Node(0, Node(1, Node(2, Node(3, None))))
    assert max(linked_list) == 3


def test_max_non_empty_scrambled() -> None:
    """Max of a scrambled linked list should return the maximum value."""
    linked_list = Node(1, Node(3, Node(2, Node(0, None))))
    assert max(linked_list) == 3


def test_linkify_empty() -> None:
    """Linkify should return None if input list is empty."""
    assert linkify([]) is None
    

def test_linkify_non_empty_ordered() -> None:
    """Linkify of a non-empty list[int] should be equal to the test linked list."""
    linked_list = Node(0, Node(1, Node(2, Node(3, None))))
    assert is_equal(linkify([0, 1, 2, 3]), linked_list)


def test_linkify_non_empty_scrambled() -> None:
    """Another use-case test for linkify."""
    linked_list = Node(2, Node(3, Node(0, Node(1, None))))
    assert is_equal(linkify([2, 3, 0, 1]), linked_list)


def test_scale_empty() -> None:
    """Scale of an empty linked list should return None."""
    assert scale(None, 2) is None


def test_scale_non_empty() -> None:
    """Scale of a non-empty linked list should return a properly scaled new linked list."""
    linked_list = linkify([0, 2, 4, 6])
    assert is_equal(linked_list, scale(linkify([0, 1, 2, 3]), 2))