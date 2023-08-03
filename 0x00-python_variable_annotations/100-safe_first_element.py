#!/usr/bin/env python3
"""
Created by Jenaide Sibolie
"""
from typing import Any, Union, Sequence



def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """
    a function that retrieves the first element of a sequence if it exists.
    """
    if lst:
        return lst[0]
    else:
        return None
