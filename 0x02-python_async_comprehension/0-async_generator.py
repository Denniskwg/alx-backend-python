#!/usr/bin/env python3

"""0-async_generator defines a function async_generator
imports asyncio and random module
"""
import asyncio
import random


async def async_generator() -> float:
    """loops 10 times, each time asynchronously
    wait 1 second, then yield a random number
    between 0 and 10
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
