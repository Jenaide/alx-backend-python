#!/usr/bin/env python3
"""
Created by Jenaide Sibolie
"""
import unittest
from parameterized import parameterized
from utils import (
        access_nested_map,
        get_json,
        memoize)


class TestAccessNestedMap(unittest.TestCase):
    """
    testing the access_nested_map function
    """
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(self, nested_map, path, expected):
        result = access_nested_map(nested_map, path)
        self.assertEqual(result, expected)
