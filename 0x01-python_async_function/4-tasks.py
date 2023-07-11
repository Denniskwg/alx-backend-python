#!/usr/bin/env python3
import asyncio
from typing import List
task_wait_random = __import__('3-tasks').task_wait_random
"""4-tasks defines a function task_wait_n
that spawns wait_random imported from 0-basic_async_syntax
a number of times
"""


Vector = List[float]


async def task_wait_n(n: int, max_delay: int) -> Vector:
    """spawns task_wait_random n times with max_delay
    and returns a list of delays
    """
    tasks = [task_wait_random(max_delay) for _ in range(n)]
    results = await asyncio.gather(*tasks)
    return sorted(results)
