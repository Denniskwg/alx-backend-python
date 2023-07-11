#!/usr/bin/env python3
import asyncio
import time
wait_n = __import__('1-concurrent_coroutines').wait_n
"""2-measure_runtime defines a function measure_time
and imports wait_n from ./1-concurrent_coroutines
"""


def measure_time(n: int, max_delay: int) -> float:
    """measures the time taken to run wait_n
    n times with a max delay of max_delay
    """
    start_time = time.time()
    asyncio.run(wait_n(n, max_delay))
    end_time = time.time()
    total_time = end_time - start_time
    return total_time / n
