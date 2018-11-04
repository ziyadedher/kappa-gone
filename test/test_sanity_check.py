"""Simple sanity check tests.

This module consists of very simple sanity checks just to make sure
the testing suite and continuous integration reaches the testing phase.
"""
from typing import TypeVar

from hypothesis import given
from hypothesis.strategies import integers, floats


class TestAdding:
    T = TypeVar('T', int, float)

    def add_two_numbers(self, number_one: T, number_two: T) -> T:
        return number_one + number_two

    @given(integers(), integers())
    def test_add_integers(self, int_one: int, int_two: int) -> None:
        assert self.add_two_numbers(int_one, int_two) == int_one + int_two

    @given(floats(allow_nan=False, allow_infinity=False),
           floats(allow_nan=False, allow_infinity=False))
    def test_add_reals(self, real_one: float, real_two: float) -> None:
        assert self.add_two_numbers(real_one, real_two) == real_one + real_two
