#!/usr/bin/env python3
"""Created by Jenaide Sibolie
"""
from importlib import import_module as using
from typing import List


async_generator = using('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """
    a function that creates a list of 10 numbers from a 10-number generator.
    """
    return [num async for num in async_generator()]
