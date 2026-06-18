#!/usr/bin/env python3
"""
This module provides an asynchronous coroutine that handles random delays.

It demonstrates the basic syntax of async and await in Python by simulating
an I/O-bound operation using a random float duration.
"""

import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """
    Wait for a random delay between 0 and max_delay seconds and return it.

    Args:
        max_delay (int): The maximum number of seconds to wait. Default is 10.

    Returns:
        float: The actual amount of time spent waiting.
    """
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
