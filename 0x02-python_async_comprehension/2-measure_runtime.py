#!/usr/bin/env python3

""" Coroutine executes async_comprehension four times in
parallel using asyncio.gather. """

import asyncio
import time

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """Executes async_comprehension four times in parallel
    and measures total runtime.

    Returns:
        float: The total runtime in seconds.
    """
    # Record the start time
    initial_time = time.perf_counter()

    # Run async_comprehension four times in parallel
    await asyncio.gather(*(async_comprehension() for _ in range(4)))

    total_time = time.perf_counter() - initial_time  # Record the end time
    return total_time   # Calculate and return the total runtime
