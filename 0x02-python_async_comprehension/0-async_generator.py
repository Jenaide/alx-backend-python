#!/usr/bin/env python3
""" Created by Jenaide Sibolie
"""
import asyncio
import random

async def async_generator() -> Generator[float, None, None]:
    """
    async function that generates a sequence of 10 numbers
    """
    for _ in range(10):
        await asyncio.sleep(1)  # Asynchronously wait for 1 second
        yield random.randint(0, 10)  # Yield a random number between 0 and 10
