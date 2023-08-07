#!/usr/bin/env python3
"""
Created by Jenaide Sibolie
"""
import asyncio
import random


async def wait_random(max_delay=10):
    """
    an asynchronous coroutine that takes in an int arg, that waits for a
    random delay between 0 and 10 seconds and eventually returns it.
    """
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
