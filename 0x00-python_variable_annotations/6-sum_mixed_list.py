#!/usr/bin/env python3
"""
Created by Jenaide Sibolie
"""
from typing import List, Union

def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    function that takes a list of integers and floats
    and returns their sum as a float
    """
    return float(sum(mxd_lst))
