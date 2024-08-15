from test_fizz_buzz import TestFizzBuzz, TestFizzBuzzQA, TestFizzBuzzOutros
from test_remover_duplicado import TestRemoverDuplicado, TestRemoverDuplicadoQA, TestRemoverDuplicadoOutros
import unittest


def suite_fizz_buzz():
    test_suite = unittest.TestSuite()
    test_suite.addTest(unittest.TestLoader().loadTestsFromTestCase(TestFizzBuzz))
    test_suite.addTest(unittest.TestLoader().loadTestsFromTestCase(TestFizzBuzzQA))
    test_suite.addTest(unittest.TestLoader().loadTestsFromTestCase(TestFizzBuzzOutros))
    return test_suite


def suite_remover_duplicado():
    test_suite = unittest.TestSuite()
    test_suite.addTest(unittest.TestLoader().loadTestsFromTestCase(TestRemoverDuplicado))
    test_suite.addTest(unittest.TestLoader().loadTestsFromTestCase(TestRemoverDuplicadoQA))
    test_suite.addTest(unittest.TestLoader().loadTestsFromTestCase(TestRemoverDuplicadoOutros))
    return test_suite


if __name__ == '__main__':
    # mySuit = suite_fizz_buzz()
    mySuit = suite_remover_duplicado()

    runner = unittest.TextTestRunner(verbosity=2, failfast=False)
    runner.run(mySuit)
