#!/usr/bin/env python3
from typing import List, Union
"""6-sum_mixed_list defines a function sum_mixed_list
which takes a list mxd_lst of integers and floats
and returns their sum as a float
"""

Vector = List[Union[int, float]]


def sum_mixed_list(sum_mixed_list: Vector) -> float:
    return sum(sum_mixed_list)
