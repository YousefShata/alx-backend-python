#!/usr/bin/env python3
"""
element_length  module
"""
from typing import List, Tuple


def element_length(lst: List[str]) -> List[Tuple[str, int]]:
    """
    element length function
    """
    return [(i, len(i)) for i in lst]
