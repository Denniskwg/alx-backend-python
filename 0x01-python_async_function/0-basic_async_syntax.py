#!/usr/bin/env python3
import asyncio
import random
"""0-basic_async_syntax

"""


async def wait_random(max_delay: int = 10) -> float:
    """waits for a random delay and eventually returns
    the delay
    """
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
