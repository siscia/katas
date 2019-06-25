
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

#import re
#tokens = ['(', ')', 'x', '*', '+', '-', '/', 'sin', 'cos', '^', 'ln', r'[0-9]+', r'\w+']
#tokens = [re.compile(i) for i in tokens]

def parse(text):
    text = text.replace('(', '( ').replace(')', ' )')
    tokens = text.split()
    retval = []
    it = iter(tokens)
    def internal_parse(it):
        ret = []
        for tok in it:
            print(tok)
            if tok == '(':
                ret.append(internal_parse(it))
            elif tok == ')':
                return ret
            elif tok.isdigit():
                ret.append(int(tok))
            elif not tok:
                continue
            else:
                ret.append(tok)
        return ret
    return internal_parse(it)[0]

def dump(text):
    return text

class TestGoal(unittest.TestCase):
    #def test_working(self):
    #    self.assertEqual(1 + 1, 2)

    def test_to_datastructure(self):
        self.assertEqual(dump(parse("(* x 2)")), ['*', 'x', 2])
        self.assertEqual(dump(parse("(* x 12)")), ['*', 'x', 12])
        self.assertEqual(dump(parse("(+ (* x 12) (* x 2))")), ['+' ['*', 'x', 12], ['*', 'x', 2]])

    #def test_goal(self):
    #    self.assertEqual(differentiate("(^ x 2)"), "(* 2 x)")


# to run `python3 differentation.py`
if __name__ == '__main__':
    unittest.main()

