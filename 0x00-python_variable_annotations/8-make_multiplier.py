#!/usr/bin/env python3
"""
Created by Jenaide Sibolie
"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    A multiplier function
    """
    return lambda x: x * multiplier
