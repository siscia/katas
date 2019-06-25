#!/bin/env python3

import unittest

"""
Symbolic differentiation rules; assume to differentiate for variable x
https://www.codewars.com/kata/symbolic-differentiation-of-prefix-expressions/train/python

Examples:
 - f(x) == (f x) => f'(x)
 - (cos x) => (- (sin x))
 - (sin x) => (cos x)
 - (* n x) => n
 - (* n (^ x m) => (* n (* m (^ x (- m 1))))
 - (* (f n) (g n)) => (+ (* (f' x) (g x)) (* (g' x) (f x)))
"""


def product_rule(a, b):
    return ['+', ['*', diff(a), b], ['*', a, diff(b)]]


def diff(formula):
    if isinstance(formula, int):
        return 0
    if formula == 'x': return 1
    if formula[0] == "*":
        return product_rule(formula[1], formula[2])
    return formula


def simplify(formula):
    if not isinstance(formula, list):
        return formula
    formula = [simplify(i) for i in formula]
    if formula[0] == "*":
        if formula[1] == 0 or formula[2] == 0:
            return 0
        elif formula[1] == 1:
            return formula[2]
        elif formula[2] == 1:
            return formula[1]
        elif isinstance(formula[1], int) and isinstance(formula[2], int):
            return formula[1] * formula[2]
        else:
            return formula
    elif formula[0] == "+":
        if formula[1] == 0:
            return formula[2]
        elif formula[2] == 0:
            return formula[1]
        elif isinstance(formula[1], int) and isinstance(formula[2], int):
            return formula[1] + formula[2]
        else:
            return formula
    else:
        return formula


def differentiate(s):
    formula = simplify(parse(s))
    return simplify(diff(formula))


def parse(text):
    text = text.replace('(', '( ').replace(')', ' )')
    tokens = text.split()
    it = iter(tokens)

    def internal_parse(it):
        ret = []
        for tok in it:
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
    # print(text)
    return text


class TestGoal(unittest.TestCase):

    def test_to_datastructure(self):
        self.assertEqual(dump(parse("(* x 2)")), ['*', 'x', 2])
        self.assertEqual(dump(parse("(* x 12)")), ['*', 'x', 12])
        self.assertEqual(dump(parse("(+ (* x 12) (* x 2))")), ['+', ['*', 'x', 12], ['*', 'x', 2]])

    def test_simplify(self):
        self.assertEqual(simplify(['*', 0, 'x']), 0)
        self.assertEqual(simplify(['*', 'x', 0]), 0)
        self.assertEqual(simplify(['*', 'x', 1]), 'x')
        self.assertEqual(simplify(['*', 1, 'x']), 'x')
        self.assertEqual(simplify(['*', 1, 2]), 2)
        self.assertEqual(simplify(['*', 2, 3]), 6)
        self.assertEqual(simplify(3), 3)
        self.assertEqual(simplify('x'), 'x')

        self.assertEqual(simplify(['+', 0, 'x']), 'x')
        self.assertEqual(simplify(['+', 'x', 0]), 'x')
        self.assertEqual(simplify(['+', 3, 2]), 5)

    def test_mult_diff(self):
        self.assertEqual(dump(parse("(* x 2)")), ['*', 'x', 2])
        self.assertEqual(differentiate("(* x 2)"), 2)
        self.assertEqual(dump(parse("(* 2 x)")), ['*', 2, 'x'])
        self.assertEqual(differentiate("(* 2 x)"), 2)
        self.assertEqual(dump(parse("(* x (* 2 x))")), ['*', 'x', ['*', 2, 'x']])
        self.assertEqual(differentiate("(* x (* 2 x))"), ['+', ['*', 2, 'x'], ['*', 'x', 2]])

    # def test_goal(self):
    #    self.assertEqual(differentiate("(^ x 2)"), "(* 2 x)")


# to run `python3 differentation.py`
if __name__ == '__main__':
    unittest.main()

    # unittest command for Jupyter notebooks:
    # unittest.main(argv=['first-arg-is-ignored'], exit=False)
