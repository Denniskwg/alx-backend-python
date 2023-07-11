#!/usr/bin/env python3
import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random
"""1-concurrent_coroutines defines a function wait_n
that spawns wait_random imported from 0-basic_async_syntax
a number of times
"""


Vector = List[float]


async def wait_n(n: int, max_delay: int) -> Vector:
    """spawns wait_random n times with max_delay
    and returns a list of delays
    """
    tasks = [wait_random(max_delay) for _ in range(n)]
    results = await asyncio.gather(*tasks)
    return sorted(results)
