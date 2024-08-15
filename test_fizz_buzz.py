import unittest
from generic import Generic
from fizz_buzz import fizz_buzz


def main(num: int):
    return fizz_buzz(num=num)


class TestFizzBuzz(unittest.TestCase):

    def test_num_01(self):
        num = 1
        ret = main(num=num)
        Generic.assert_default_fizz_buzz(source=ret, source_len=num)
        self.assertEqual(ret, ['1'])

    def test_num_02(self):
        num = 2
        ret = main(num=num)
        Generic.assert_default_fizz_buzz(source=ret, source_len=num)
        self.assertEqual(ret, ['1', '2'])

    def test_num_03(self):
        num = 3
        ret = main(num=num)
        Generic.assert_default_fizz_buzz(source=ret, source_len=num)
        self.assertEqual(ret, ['1', '2', 'Fizz'])

    def test_num_04(self):
        num = 4
        ret = main(num=num)
        Generic.assert_default_fizz_buzz(source=ret, source_len=num)
        self.assertEqual(ret, ['1', '2', 'Fizz', '4'])

    def test_num_05(self):
        num = 5
        ret = main(num=num)
        Generic.assert_default_fizz_buzz(source=ret, source_len=num)
        self.assertEqual(ret, ['1', '2', 'Fizz', '4', 'Buzz'])

    def test_num_06(self):
        num = 6
        ret = main(num=num)
        Generic.assert_default_fizz_buzz(source=ret, source_len=num)
        self.assertEqual(ret, ['1', '2', 'Fizz', '4', 'Buzz', 'Fizz'])

    def test_num_07(self):
        num = 7
        ret = main(num=num)
        Generic.assert_default_fizz_buzz(source=ret, source_len=num)
        self.assertEqual(ret, ['1', '2', 'Fizz', '4', 'Buzz', 'Fizz', '7'])

    def test_num_08(self):
        num = 8
        ret = main(num=num)
        Generic.assert_default_fizz_buzz(source=ret, source_len=num)
        self.assertEqual(ret, ['1', '2', 'Fizz', '4', 'Buzz', 'Fizz', '7', '8'])

    def test_num_09(self):
        num = 9
        ret = main(num=num)
        Generic.assert_default_fizz_buzz(source=ret, source_len=num)
        self.assertEqual(ret, ['1', '2', 'Fizz', '4', 'Buzz', 'Fizz', '7', '8', 'Fizz'])

    def test_num_10(self):
        num = 10
        ret = main(num=num)
        Generic.assert_default_fizz_buzz(source=ret, source_len=num)
        self.assertEqual(ret, ['1', '2', 'Fizz', '4', 'Buzz', 'Fizz', '7', '8', 'Fizz', 'Buzz'])

    def test_num_11(self):
        num = 11
        ret = main(num=num)
        Generic.assert_default_fizz_buzz(source=ret, source_len=num)
        self.assertEqual(ret, ['1', '2', 'Fizz', '4', 'Buzz', 'Fizz', '7', '8', 'Fizz', 'Buzz', '11'])

    def test_num_12(self):
        num = 12
        ret = main(num=num)
        Generic.assert_default_fizz_buzz(source=ret, source_len=num)
        self.assertEqual(ret, ['1', '2', 'Fizz', '4', 'Buzz', 'Fizz', '7', '8', 'Fizz', 'Buzz', '11', 'Fizz'])

    def test_num_13(self):
        num = 13
        ret = main(num=num)
        Generic.assert_default_fizz_buzz(source=ret, source_len=num)
        self.assertEqual(ret, ['1', '2', 'Fizz', '4', 'Buzz', 'Fizz', '7', '8', 'Fizz', 'Buzz', '11', 'Fizz', '13'])

    def test_num_14(self):
        num = 14
        ret = main(num=num)
        Generic.assert_default_fizz_buzz(source=ret, source_len=num)
        self.assertEqual(ret, ['1', '2', 'Fizz', '4', 'Buzz', 'Fizz', '7', '8', 'Fizz', 'Buzz', '11', 'Fizz', '13', '14'])

    def test_num_15(self):
        num = 15
        ret = main(num=num)
        Generic.assert_default_fizz_buzz(source=ret, source_len=num)
        self.assertEqual(ret, ['1', '2', 'Fizz', '4', 'Buzz', 'Fizz', '7', '8', 'Fizz', 'Buzz', '11', 'Fizz', '13', '14', 'FizzBuzz'])

    def test_exception_str(self):
        with self.assertRaises(Exception): main(num='')

    def test_exception_str_int(self):
        with self.assertRaises(Exception): main(num='5')

    def test_exception_none(self):
        with self.assertRaises(Exception): main(num=None)

    def test_exception_list(self):
        with self.assertRaises(Exception): main(num=[])

    def test_exception_negtivo(self):
        with self.assertRaises(Exception): main(num=-5)

    def test_exception_zero(self):
        with self.assertRaises(Exception): main(num=0)


class TestFizzBuzzQA(unittest.TestCase):
    pass


class TestFizzBuzzOutros(unittest.TestCase):
    pass
