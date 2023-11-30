#!/usr/bin/env python3
"""
@Author: Kęstutis Gustaitis kestutis.gustaitis@gmail.com
@Date: 2023.11.30
"""

from utils import clear_terminal, digits_in_number, is_puzzle_solvable
import random

class Board:
    def __init__(self, dimension = 4):
        self.dimension = dimension
        self.size = self.dimension * self.dimension
        self.last_index = self.size - 1
        self.max_digits = digits_in_number(self.last_index)
        self.board = self._new_game_board()

    def _new_game_board(self):
        """
        Creates new solvable, but unsolved game board with number zero
        representing blank/empty cell.
        """
        available_values = []
        game_board = []
        for i in range(self.dimension * self.dimension):
            available_values.append(i)
        for i in range(self.dimension):
            row = []
            for j in range(self.dimension):
                value = available_values.pop(random.randint(0, len(available_values) - 1))
                row.append(value)
            game_board.append(row)

        redo = self.is_puzzle_solved(game_board) or not is_puzzle_solvable(game_board, self.dimension)
        return game_board if not redo else self._new_game_board()

    def is_puzzle_solved(self, board):
        """
        Takes two dimension array and checks if numbers are ordered in it.
        """
        for i in range(self.dimension):
            for j in range(self.dimension):
                if i == self.dimension - 1 and j == self.dimension - 1:
                    continue # ignore last cell
                if board[i][j] != (1 + j) + i * self.dimension:
                    return False
        return True

    def _print_separating_line(self):
        """
        Prints line like:
        `+---+---+---+---+`
        """
        line = '+'
        for i in range(self.dimension):
            for j in range(self.max_digits):
                line += '-'
            line += '+'  # symbol between numbers
        print(line)

    def _print_row(self, board_row):
        line = '|'
        for number in board_row:
            number_of_additional_spaces = self.max_digits - digits_in_number(number)
            for i in range(number_of_additional_spaces):
                line += ' '
            if number == 0:
                line += ' '
            else:
                line += str(number)
            line += '|'
        print(line)
        self._print_separating_line()

    def print_board(self):
        """
        Prints board in terminal.
        """
        clear_terminal()
        print('Play game by moving zero/blank cell using arrow buttons in your keyboard.\n`Esc` to terminate game.')
        self._print_separating_line()
        for i in range(self.dimension):
            self._print_row(self.board[i])
        if self.is_puzzle_solved(self.board):
            print('Congrats you have solved the puzzle :)')
            exit()

    def move_up(self):
        """
        Checks if move is possible and switches zero/blank cell with cell above it.
        Otherwise prints error.
        """
        for x in range(self.dimension):
            for y in range(self.dimension):
                if self.board[x][y] == 0:
                    if x == 0:
                        self.print_board()
                        print('Empty cell is already at the top.')
                        return
                    self.board[x][y], self.board[x-1][y] = self.board[x-1][y], self.board[x][y]
                    self.print_board()
                    return

    def move_down(self):
        """
        Checks if move is possible and switches zero/blank cell with cell below it.
        Otherwise prints error.
        """
        for x in range(self.dimension):
            for y in range(self.dimension):
                if self.board[x][y] == 0:
                    if x == self.dimension - 1:
                        self.print_board()
                        print('Empty cell is already at the bottom.')
                        return
                    self.board[x][y], self.board[x+1][y] = self.board[x+1][y], self.board[x][y]
                    self.print_board()
                    return

    def move_right(self):
        """
        Checks if move is possible and switches zero/blank cell with cell to the right of it.
        Otherwise prints error.
        """
        for x in range(self.dimension):
            for y in range(self.dimension):
                if self.board[x][y] == 0:
                    if y == self.dimension - 1:
                        self.print_board()
                        print('Empty cell is already at the very right of the board.')
                        return
                    self.board[x][y], self.board[x][y+1] = self.board[x][y+1], self.board[x][y]
                    self.print_board()
                    return

    def move_left(self):
        """
        Checks if move is possible and switches zero/blank cell with cell to the left of it.
        Otherwise prints error.
        """
        for x in range(self.dimension):
            for y in range(self.dimension):
                if self.board[x][y] == 0:
                    if y == 0:
                        self.print_board()
                        print('Empty cell is already at the very left of the board.')
                        return
                    self.board[x][y], self.board[x][y-1] = self.board[x][y-1], self.board[x][y]
                    self.print_board()
                    return
