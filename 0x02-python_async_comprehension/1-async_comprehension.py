#!/usr/bin/env python3
"""1-async_comprehension defines a function async_comprehension
and imports async_generator from ./0-async_generator
"""

import asyncio
from typing import List
async_generator = __import__('0-async_generator').async_generator

Vector = List[float]


async def async_comprehension() -> Vector:
    """returns a list of random numbers generated
    from calling async_generator
    """
    return [i async for i in async_generator()]
