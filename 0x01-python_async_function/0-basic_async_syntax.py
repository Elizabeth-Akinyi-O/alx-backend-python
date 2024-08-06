#!/usr/bin/env python3

"""
Asynchronous coroutine that takes in an integer argument
that waits for a random delay and eventually returns it. """

import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """ Waits for a random delay between 0 and
    max_delay and eventually returns it. """
    wait_time = random.uniform(0, max_delay)
    await asyncio.sleep(wait_time)
    return wait_time
