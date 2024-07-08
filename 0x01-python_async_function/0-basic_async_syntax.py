#!/usr/bin/env python3
"""
make random
"""
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """
    wait for random delay
    """
    await asyncio.sleep(max_delay)
    return random.uniform(0, max_delay)
