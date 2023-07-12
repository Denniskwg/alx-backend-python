#!/usr/bin/env python3
"""3-tasks defines a function task_wait_random and imports
wait_random from ./0-basic_async_syntax and asyncio module
"""

import asyncio
from asyncio import Task
wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> Task:
    """returns a asyncio.Task
    """
    task = asyncio.ensure_future(wait_random(max_delay))
    return task
