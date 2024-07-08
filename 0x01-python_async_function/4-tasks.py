#!/usr/bin/env python3
"""
tasks
"""
import asyncio
import random
from typing import List
task_wait_random = __import__('3-tasks').task_wait_random

async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    use random generator fucntion N of times
    """
    tasks = [task_wait_random(max_delay) for _ in range(n)]
    delay_List = await asyncio.gather(*tasks)
    return sorted(delay_List)
