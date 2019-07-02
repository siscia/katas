#!/bin/env python3

import unittest

values = dict()
values[0] = 0
values[1] = 1



def fib (x):
	if x not in values:
		for i in range(len(values), x+1):
			values[i] = values[i-1] + values[i-2]
	return values[x]

def negfib(x: int) -> int:
    # negfib(x) = negfib(x + 2) - negfib(x + 1)

    tempx_2 = 1 # fib(1)
    tempx_1 = 0 # fib(0)

    for i in range(-1, x-1, -1):
        tx = tempx_2 - tempx_1
        tempx_2 = tempx_1
        tempx_1 = tx

    return tempx_1

def fib2 (x):
	temp_2 = 0
	temp_1 = 1
	if x== 0:
		return 0
	elif x== 1:
		return 1
	else:
		pass
	for i in range(2, x+1):
		tx = temp_2 + temp_1
		temp_2 = temp_1
		temp_1 = tx

	return temp_1


class TestGoal(unittest.TestCase):
    def test_to_datastructure(self):
        self.assertEqual(fib2(0),0)
        self.assertEqual(fib2(1),1)
        self.assertEqual(fib2(2),1)
        self.assertEqual(fib2(3),2)
        self.assertEqual(fib2(4),3)

    def test_jumping(self):
        self.assertEqual(fib2(3),2)
        self.assertEqual(fib2(4),3)
        self.assertEqual(fib2(6),8)
        self.assertEqual(fib2(50),12586269025)
        self.assertEqual(fib2(2000000),12586269025)
        

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
