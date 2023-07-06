#!/usr/bin/env python3
from typing import Callable
"""8-make_multiplier defines a function make_multiplier
that takes a float multiplier as argument and returns a
function that multiplies a float by multiplier
"""


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    def func(num: float):
        return num * multiplier
    return func
