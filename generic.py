from enum import StrEnum
import unittest


class Generic:
    @staticmethod
    def assert_default_fizz_buzz(source: list, source_len: int) -> None:
        unittest.TestCase().assertIsInstance(source, list)
        unittest.TestCase().assertEqual(len(source), source_len)
        for element in source:
            unittest.TestCase().assertIsInstance(element, str)

    @staticmethod
    def assert_default_remover_duplicado(source: list, ret_list: list, expected: list) -> None:
        unittest.TestCase().assertIsInstance(ret_list, list)
        unittest.TestCase().assertEqual(len(ret_list), len(expected))
        for element in ret_list:
            unittest.TestCase().assertIsInstance(element, int)
        unittest.TestCase().assertEqual(ret_list, expected)
