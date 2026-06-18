#!/usr/bin/env python3
"""
This module provides a function to measure the execution time of an
asynchronous coroutine that spawns multiple concurrent tasks.
"""

import asyncio
import time

wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    Measure the average execution time for running wait_n n times.

    Args:
        n (int): The number of times to spawn the wait_random coroutine.
        max_delay (int): The maximum delay for each coroutine.

    Returns:
        float: The total execution time divided by n.
    """
    start_time = time.perf_counter()
    asyncio.run(wait_n(n, max_delay))
    end_time = time.perf_counter()

    total_time = end_time - start_time
    return total_time / n
