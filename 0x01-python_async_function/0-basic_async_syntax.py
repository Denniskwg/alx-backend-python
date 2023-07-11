#!/usr/bin/env python3
import asyncio
import random
"""0-basic_async_syntax defines a function
wait_random that waits for a random delay and
returns the delay
"""


async def wait_random(max_delay: int = 10) -> float:
    """waits for a random delay and eventually returns
    the delay
    """
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
