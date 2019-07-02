#!/bin/env python3

import unittest


def negfib(x: int) -> int:
    # negfib(x) = negfib(x + 2) - negfib(x + 1)

    tempx_2 = 1 # fib(1)
    tempx_1 = 0 # fib(0)

    for i in range(-1, x-1, -1):
        tx = tempx_2 - tempx_1
        tempx_2 = tempx_1
        tempx_1 = tx

    return tempx_1


class TestGoal(unittest.TestCase):

    def test_negative_fibonacci(self):
        #self.assertEqual(negfib(2), 1)
        #self.assertEqual(negfib(1), 1)
        #self.assertEqual(negfib(0), 0)
        self.assertEqual(negfib(-1), 1)
        self.assertEqual(negfib(-2), -1)
        self.assertEqual(negfib(-3), 2)
        self.assertEqual(negfib(-4), -3)
        self.assertEqual(negfib(-5), 5)
        self.assertEqual(negfib(-6), -8)
        self.assertEqual(negfib(-7), 13)
        self.assertEqual(negfib(-8), -21)
        self.assertEqual(negfib(-5001), -21)


# to run `python3 differentation.py`
if __name__ == '__main__':
    unittest.main()

    # unittest command for Jupyter notebooks:
    # unittest.main(argv=['first-arg-is-ignored'], exit=False)
