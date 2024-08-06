#!/usr/bin/env python3

""" Execute multiple coroutines at the same time with async. """

import asyncio
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """Spawn wait_random function n times

    Args:
        n (int): number of time wait _random should be callled.
        max_delay (int): delay period

    Returns:
        List[float]: List of all the delays in sorted order
    """
    tasks = [wait_random(max_delay) for _ in range(n)]
    # Run the tasks concurrently and collect the results
    wait_time = await asyncio.gather(*tasks)
    # Sort the results in ascending order
    sorted_wait_time = []
    while wait_time:
        min_delay = min(wait_time)
        sorted_wait_time.append(min_delay)
        wait_time.remove(min_delay)
    return sorted_wait_time
