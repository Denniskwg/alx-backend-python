#!/usr/bin/env python3
import asyncio
import time
async_comprehension = __import__('1-async_comprehension').async_comprehension
"""defines a function measure_runtime, imports asyncio and time modules and
function async_comprehension from 1-async_comprehension
"""


async def measure_runtime() -> float:
    """runs async_comprehension four times in parallel
    and measures the total tome taken
    """
    start = time.time()
    tasks = [async_comprehension() for _ in range(4)]
    await asyncio.gather(*tasks)
    end = time.time()
    total = end - start
    return total
