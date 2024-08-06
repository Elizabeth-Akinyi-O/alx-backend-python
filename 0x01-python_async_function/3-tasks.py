#!/usr/bin/env python3

""" Returns a asyncio.Task. """

import asyncio


wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """Create task wait random

    Args:
        max_delay (int): delay period

    Returns:
        (asyncio.Task)
    """
    async_task = asyncio.create_task(wait_random(max_delay))

    return async_task


""" # OTHER METHOD #
async def main():
# Creates a task with a maximum delay of 5 seconds
async_task = task_wait_random(5)
# Optionally await the task if you want to wait for its completion
 await async_task

asyncio.run(main())"""
