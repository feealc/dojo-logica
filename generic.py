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

    @staticmethod
    def assert_default_inverter_rgb(source: tuple, expected: tuple) -> None:
        unittest.TestCase().assertIsInstance(source, tuple)
        unittest.TestCase().assertEqual(len(source), len(expected))
        red, blue, green = source
        unittest.TestCase().assertIsInstance(red, int)
        unittest.TestCase().assertTrue(0 <= red <= 255)
        unittest.TestCase().assertIsInstance(green, int)
        unittest.TestCase().assertTrue(0 <= green <= 255)
        unittest.TestCase().assertIsInstance(blue, int)
        unittest.TestCase().assertTrue(0 <= blue <= 255)
        unittest.TestCase().assertEqual(source, expected)
