#!/usr/bin/env python3

""" Measures the runtime of coroutines. """

import time
import asyncio

wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """ Measures the total execution time for wait_n(n, max_delay)

    Args:
        n (int): number of time wait _random should be callled.
        max_delay (int): delay period

    Returns:
        float: total execution time / n
    """
    # Record the start time
    t0 = time.time()  # Record the start time
    # Run the event loop and measure the time taken by wait_n
    asyncio.run(wait_n(n, max_delay))
    t1 = time.time()  # Record the end time
    total_time = t1 - t0  # Calculate the total time taken
    return total_time / n  # Return the average time per coroutine
