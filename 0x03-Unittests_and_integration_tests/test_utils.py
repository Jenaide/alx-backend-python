#!/usr/bin/env python3
"""
Created by Jenaide Sibolie
"""
import unittest
from parameterized import parameterized
from typing import Dict, Tuple, Union
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
        ({}, ("a",), KeyError),
        ({"a": 1}, ("a", "b"), KeyError),
    ])
    def test_access_nested_map_exception(self, nested_map: Dict, path: Tuple[str], exception: Exception) -> None:
        """
        test case ofaccess_nested_map exception raising
        """
        with self.assertRaises(exception):
            access_nested_map(nested_map, path)

class TestGetJson(unittest.TestCase):
    """ test case for the get_json function """
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False}),
    ])
    def test_get_json(
            self,
            test_url: str,
            test_payload: Dict,) -> None:
        """ testing the get_json output """
        values = {'json.return_value': test_payload}
        with patch('requests.get', return_value=Mock(**values)) as request_get:
            self.assertEqual(get_json(test_url), test_payload)
            request_get.asser_called_once_with(test_url)
