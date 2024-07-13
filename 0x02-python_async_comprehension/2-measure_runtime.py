#!/usr/bin/env python3
"""
async_comprehension module
"""
import asyncio
import time
from typing import AsyncGenerator
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    run function async_comprehension 4 times
    """

    start_time = time.time()
    await asyncio.gather(*(async_comprehension() for _ in range(4)))
    end_time = time.time()
    elapsed_time = end_time - start_time

    return elapsed_time
