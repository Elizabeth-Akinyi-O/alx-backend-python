#!/usr/bin/env python3

""" Executes multiple coroutines at the same time with async. """

import asyncio
from typing import List


wait_random = __import__('0-basic_async_syntax').wait_random
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """Spawn task_wait_random function n times

    Args:
        n (int): Number of times task_wait_random should be called.
        max_delay (int): Maximum delay period.

    Returns:
        List[float]: List of all the delays in sorted order.
    """
    # Create a list of asyncio tasks
    tasks = [task_wait_random(max_delay) for _ in range(n)]
    # Run the tasks concurrently and collect the results
    wait_times = await asyncio.gather(*tasks)
    # Sort the results in ascending order
    sorted_wait_times = []
    while wait_times:
        min_delay = min(wait_times)
        sorted_wait_times.append(min_delay)
        wait_times.remove(min_delay)
    return sorted_wait_times
