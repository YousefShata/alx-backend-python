#!/usr/bin/env python3
"""
concurrency
"""
import asyncio
import random
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    use random generator fucntion N of times
    """
    tasks = [wait_random(max_delay) for _ in range(n)]
    delay_List = await asyncio.gather(*tasks)
    return sorted(delay_List)
