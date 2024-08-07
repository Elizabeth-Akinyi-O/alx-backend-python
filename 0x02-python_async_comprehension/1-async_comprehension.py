#!/usr/bin/env python3

""" Async Comprehensions. """

import asyncio
from typing import List

async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """Collects 10 random numbers using async comprehension.

    Returns:
        List[float]: A list containing 10 random numbers.
    """
    return [rand_numb async for rand_numb in async_generator()]
