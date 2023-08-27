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
        """
        tests access_nested_map output
        """
        result = access_nested_map(nested_map, path)
        self.assertEqual(result, expected)

    @parameterized.expand([
        ({}, ("a",), "a"),
        ({"a": 1}, ("a", "b"), "b"),
    ])
    def test_access_nested_map_exception(self, nested_map, path, expected_exception_message):
        """
        test case ofaccess_nested_map exception raising
        """
        with self.assertRaises(KeyError) as context:
            access_nested_map(nested_map, path)
        self.assertEqual(str(context.exception), expected_exception_message)
