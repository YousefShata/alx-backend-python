#!/usr/bin/env python3
"""
concurrency
"""
from typing import List
import asyncio
import random
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    use random generator fucntion N of times
    """
    tasks = [wait_random(max_delay) for _ in range(n)]
    delayList = await asyncio.gather(*tasks)
    return delayList
