import unittest
from generic import Generic
from remover_duplicado import remover_duplicado


def main(param: list):
    return remover_duplicado(param=param)


class TestRemoverDuplicado(unittest.TestCase):

    def run_test(self, source: list, expected: list):
        ret = main(param=source)
        Generic.assert_default_remover_duplicado(source=source, ret_list=ret, expected=expected)
        self.assertTrue(True)

    def test_1(self):
        self.run_test(source=[1, 2, 2, 4, 7], expected=[1, 2, 4, 7])

    def test_2(self):
        self.run_test(source=[1, '2', 3, 5], expected=[1, 2, 3, 5])

    def test_3(self):
        self.run_test(source=[1, 'brum', 2, '3', 3, 9, 12], expected=[1, 2, 3, 9, 12])

    def test_4_outros(self):
        self.run_test(source=[], expected=[])
        self.run_test(source=[1, '2', '2', 'brum', 3, 3], expected=[1, 2, 3])
        self.run_test(source=[1, 2, '2', 'brum', '', ' ', '33 ', 2, 5, 6, (1, 2), True], expected=[1, 2, 33, 5, 6])
        self.run_test(source=[True], expected=[])
        self.run_test(source=[{'a': 2}], expected=[])

    def test_exception_int(self):
        with self.assertRaises(Exception): main(param=7)

    def test_exception_str(self):
        with self.assertRaises(Exception): main(param='')

    def test_exception_str_int(self):
        with self.assertRaises(Exception): main(param='5')

    def test_exception_none(self):
        with self.assertRaises(Exception): main(param=None)


class TestRemoverDuplicadoQA(unittest.TestCase):
    pass


class TestRemoverDuplicadoOutros(unittest.TestCase):
    pass
