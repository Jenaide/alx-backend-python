#!/usr/bin/env python3
"""
Created by Jenaide Sibolie
"""
from typing import Union, Tuple

def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    function that takes a string, int or float as arg
    and return a tuple
    """
    return k, float(v * v)
