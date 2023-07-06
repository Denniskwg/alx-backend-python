#!/usr/bin/env python3
from typing import List
"""5-sum_list defines a function sum_list that
 takes a list input_list of floats as argument
 and returns their sum as a float.
"""


Vector = List[float]


def sum_list(input_list: Vector) -> float:
    return sum(input_list)
