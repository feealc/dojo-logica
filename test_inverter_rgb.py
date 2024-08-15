import unittest
from generic import Generic
from inverter_rgb import inverter_rgb


def main(colors: tuple):
    return inverter_rgb(colors=colors)


class TestInverterRgb(unittest.TestCase):

    def test_rgb(self):
        values = [
            ((255, 255, 255), (0, 0, 0)),
            ((0, 0, 0), (255, 255, 255)),
            ((165, 170, 221), (90, 85, 34)),
            ((10, 5, 2), (245, 250, 253)),
            ((254, 234, 222), (1, 21, 33))
        ]
        for value in values:
            source, expected = value
            Generic.assert_default_inverter_rgb(source=main(colors=source), expected=expected)

    def test_exception_red_int(self):
        with self.assertRaises(Exception): main(colors=('1', 1, 2))

    def test_exception_green_int(self):
        with self.assertRaises(Exception): main(colors=(1, 'x', 2))

    def test_exception_blue_int(self):
        with self.assertRaises(Exception): main(colors=(1, 2, 'b'))

    def test_exception_red_min_max(self):
        with self.assertRaises(Exception): main(colors=(-1, 1, 2))
        with self.assertRaises(Exception): main(colors=(287, 1, 2))

    def test_exception_green_min_max(self):
        with self.assertRaises(Exception): main(colors=(1, -10, 2))
        with self.assertRaises(Exception): main(colors=(1, 390, 2))

    def test_exception_blue_min_max(self):
        with self.assertRaises(Exception): main(colors=(1, 2, -3))
        with self.assertRaises(Exception): main(colors=(1, 2, 1000))


class TestInverterRgbQA(unittest.TestCase):
    pass


class TestInverterRgbOutros(unittest.TestCase):
    pass
