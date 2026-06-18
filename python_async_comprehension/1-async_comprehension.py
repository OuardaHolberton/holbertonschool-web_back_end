#!/usr/bin/env python3
"""
This module provides a coroutine that uses asynchronous comprehension.

It imports an asynchronous generator and collects its yielded values
into a list asynchronously, demonstrating PEP 530 concepts.
"""

from typing import List

async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """
    Collect 10 random float numbers from an asynchronous generator.

    This coroutine uses an async list comprehension to gather the values
    and returns the resulting list of floats.
    """
    return [i async for i in async_generator()]
