
# https://www.codewars.com/kata/symbolic-differentiation-of-prefix-expressions/train/python

import unittest

### differentation rules, assume to differentiate for x
### 
### f(x) == (f x) => f'(x)
### (cos x) => (- (sin x))
### (sin x) => (cos x)
### (* n x) => n
### (* n (^ x m) => (* n (* m (^ x (- m 1))))
### (* (f n) (g n)) => (+ (* (f' x) (g x)) (* (g' x) (f x)))

def differentiate(s):
    return s

class TestGoal(unittest.TestCase):
    def test_working(self):
        self.assertEqual(1 + 1, 2)

    def test_goal(self):
        self.assertEqual(differentiate("(^ x 2)"), "(* 2 x)")


# to run `python3 differentation.py`
if __name__ == '__main__':
    unittest.main()

