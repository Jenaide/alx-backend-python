#!/usr/bin/env python3
"""
Created by Jenaide Sibolie
"""
from typing import Any, Union



def safe_first_element(lst: Union[list, tuple, str]) -> Any:
    """
    a function that retrieves the first element of a sequence if it exists.
    """
    if lst:
        return lst[0]
    else:
        return None
