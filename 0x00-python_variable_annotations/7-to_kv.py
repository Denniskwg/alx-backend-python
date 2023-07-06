#!/usr/bin/python3
from typing import Tuple, Union
"""7-to_kv defines function to_kv that takes a string k
and an int OR float v as arguments and returns a tuple.
The first element of the tuple is the string k.
The second element is the square of the int/float v
and should be annotated as a float.
"""


def to_kv(k: str, v: Union[int, float]) -> Tuple:
    float(v)
    return (k, v**2)
