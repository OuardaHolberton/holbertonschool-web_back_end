#!/usr/bin/env python3
"""
This module provides an asynchronous generator function.

The generator yields random float numbers with an asynchronous delay,
demonstrating the basics of asynchronous programming in Python.
"""

import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """
    Loop 10 times, wait 1 second asynchronously, then yield a random number.

    Each number yielded is a random float between 0 and 10.
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
