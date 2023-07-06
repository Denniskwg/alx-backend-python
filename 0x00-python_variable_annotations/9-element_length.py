#!/usr/bin/env python3
from typing import List, Tuple, Sequence, Iterable
"""9-element_length defines a function element_length
"""


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    return [(i, len(i)) for i in lst]
