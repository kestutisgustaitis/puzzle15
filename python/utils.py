#!/usr/bin/env python3
"""
@Author: Kęstutis Gustaitis kestutis.gustaitis@gmail.com
@Date: 2023.11.30
"""

import os
import math

def clear_terminal():
    os.system('cls' if os.name=='nt' else 'clear')

def digits_in_number(number):
    """
    Returns length of digits in positive integer.
    """
    return 1 if number == 0 else int(math.log10(number)) + 1

def get_inversions_count(game_board, dimension):
    board = []
    for y in game_board:
        for x in y:
            board.append(x)
    game_board = board
    inversions_count = 0
    size = dimension * dimension
    for i in range(size - 1):
        for j in range(i + 1, size):
            if (game_board[i] != 0 and game_board[j] != 0 and game_board[i] > game_board[j]):
                inversions_count += 1
    return inversions_count

def find_zero_x_position(game_board, dimension):
    """
    Finds and returns zero/blank cell x position.
    Starts looking from bottom-right corner.
    """
    for i in range(dimension - 1, -1, -1):
        for j in range(dimension - 1, -1, -1):
            if (game_board[i][j] == 0):
                return dimension - i

def is_puzzle_solvable(game_board, dimension):
    """
    Solution is taken from https://www.geeksforgeeks.org/check-instance-15-puzzle-solvable/
    """
    inversions_count = get_inversions_count(game_board, dimension)
    if (dimension & 1):  # odd
        return ~(inversions_count & 1)
    else:  # even
        pos = find_zero_x_position(game_board, dimension)
        if (pos & 1):  # odd
            return ~(inversions_count & 1)
        else:  # even
            return (inversions_count & 1)
