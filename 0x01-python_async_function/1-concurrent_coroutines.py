#!/usr/bin/env python3
"""
Created by Jenaide Sibolie
"""
import asyncio
from typing import List


wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    funtion that excutes wait_random n time
    """
    times = await asyncio.gather(
        *tuple(map(lambda_: wait_random(max_delay), range(n))))
    return sorted(times)
