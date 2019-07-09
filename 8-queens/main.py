#!/bin/env python3

import unittest

import copy

def board(n): return [[0 for _ in range(n)] for _ in range(n)]

def place_piece(board, coord):
     x, y = coord
     new_board = copy.deepcopy(board)
     new_board[x][y] = 1
     return new_board

def remove_piece(board, coord):
    x, y = coord
    new_board = copy.deepcopy(board)
    new_board[x][y] = 0
    return new_board    

def check_diagonals(board):
    queens = {}
    for xi, row in enumerate(board):
        for yi, queen in enumerate(row):
            if queen:
                queens[(xi, yi)] = (xi, yi)
    for q1 in queens.values():
        for q2 in queens.values():
            if abs(q1[0] - q2[0]) == abs(q1[1] - q2[1]):
                return False
    return True

def valid_board(board):
    l = len(board)
    for row in range(l):
        n = 0
        for col in range(l):
            n += board[row][col]
            if n >= 2:
                return False
    for col in range(l):
        n = 0
        for row in range(l):
            n += board[row][col]
            if n >= 2:
                return False
    return check_diagonals(board)

class Test8Queens(unittest.TestCase):
    def test_empty_is_valid(self):
        self.assertTrue(valid_board(board(5)))

    def test_simple_wrong_row(self):
        wrong = [ [1, 1, 0], [0, 0, 0], [0, 0, 0] ]
        self.assertFalse(valid_board(wrong))
    
    def test_simple_wrong_col(self):
        wrong = [ [0, 1, 0], [0, 0, 0], [0, 1, 0] ]
        self.assertFalse(valid_board(wrong))

    def test_simple_wrong_diag(self):
        wrong = [ [1, 0, 0], [0, 0, 0], [0, 0, 1] ]
        self.assertFalse(valid_board(wrong))


if __name__ == '__main__':
    unittest.main()

