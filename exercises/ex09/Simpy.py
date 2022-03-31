"""Utility class for numerical operations."""

from __future__ import annotations

from typing import Union

__author__ = "730231193"


class Simpy:
    values: list[float]

    def __init__(self, values: list[float]):
        """Constructor for Simpy objects."""
        self.values = values

    def __str__(self):
        """Returns string representation of Simpy onjects."""
        return f'Simpy({self.values})'

    def fill(self, filler: float, n: int) -> None:
        """Fills values attribute with n iterations of a filler."""
        self.values = list(filler for i in range(0, n))

    def arange(self, start: float, stop: float, step: float = 1) -> None:
        """Fills values with an endpoint-not-included range of desired step size."""
        assert step != 0.0
        self.values = []
        if start < stop:
            while start < stop:
                self.values.append(start)
                start += step
        elif start > stop:
            while start > stop:
                self.values.append(start)
                start += step

    def sum(self) -> float:
        return sum(self.values)
        
    def __add__(self, rhs: Union[float, Simpy]) -> Simpy:
        """Operator override of + for Simpy objects."""
        if isinstance(rhs, float):
            rhs = Simpy(list(rhs for i in range(0, len(self.values))))
            return Simpy(list(self.values[i] + rhs.values[i] for i in range(0, len(self.values))))
        else: 
            assert len(self.values) == len(rhs.values)
            return Simpy(list(self.values[i] + rhs.values[i] for i in range(0, len(self.values))))

    def __pow__(self, rhs: Union[float, Simpy]) -> Simpy:
        """Operator override of ** for Simpy objects."""
        if isinstance(rhs, float):
            rhs = Simpy(list(rhs for i in range(0, len(self.values))))
            return Simpy(list(self.values[i] ** rhs.values[i] for i in range(0, len(self.values))))
        else:
            assert len(self.values) == len(rhs.values)
            return Simpy(list(self.values[i] ** rhs.values[i] for i in range(0, len(self.values))))

    def __eq__(self, rhs: Union[float, Simpy]) -> list[bool]:
        """Operator override of == for Simpy objects."""
        if isinstance(rhs, float):
            return list(self.values[i] == rhs for i in range(0, len(self.values)))
        else:
            assert len(self.values) == len(rhs.values)
            return list(self.values[i] == rhs.values[i] for i in range(0, len(self.values)))

    def __gt__(self, rhs: Union[float, Simpy]) -> list[bool]:
        """Operator override of > for Simpy objects."""
        if isinstance(rhs, float):
            return list(self.values[i] > rhs for i in range(0, len(self.values)))
        else:
            assert len(self.values) == len(rhs.values)
            return list(self.values[i] > rhs.values[i] for i in range(0, len(self.values)))

    def __getitem__(self, rhs: Union[int, list[bool]]) -> Union[float, Simpy]:
        """Operator override for subscription notation."""
        if isinstance(rhs, int):
            return self.values[rhs]
        else:
            assert len(self.values) == len(rhs)
            return Simpy(list(self.values[i] for i in range(0, len(self.values)) if rhs[i]))
        


            
