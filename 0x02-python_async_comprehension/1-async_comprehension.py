#!/usr/bin/env python3
"""
async_comprehension module
"""
import asyncio
import random
from typing import List
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """
    collect 10 random numbers
    """
    return [value async for value in async_generator()]
