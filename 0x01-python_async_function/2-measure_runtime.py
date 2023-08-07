#!/usr/bin/env python3
"""
Created by Jenaide Sibolie
"""
import time
import asyncio


wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    function that measures the total execution time.
    """
    start_t = time.time()
    asyncio.run(wait_n(n, max_delay))
    return (time.time() - start_t) / n
