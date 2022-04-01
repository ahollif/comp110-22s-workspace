from __future__ import annotations
from typing import Union


class StrArray:
    items: list[str]

    def __init__(self, items: list[str] = []):
        """Constructor call for StrArray."""
        self.items = items

    def __repr__(self) -> str:
        """Repr call for StrArray."""
        return f'StrArray({self.items})'

    def __add__(self, term: Union[str, StrArray]) -> StrArray:
        """Add is a vectorized operation that applies to all items."""
        if isinstance(term, str):
            return StrArray(list(item + term for item in self.items))
        else:
            assert len(self.items) == len(term.items)
            return StrArray(list(self.items[i] + term.items[i] for i in range(0, len(self.items))))


first: StrArray = StrArray(['Armando', 'Brady', 'Caleb'])
last: StrArray = StrArray(['Bacot', 'Manek', 'Love'])
print(first + '!')
print(first + last)