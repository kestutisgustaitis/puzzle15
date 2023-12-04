#!/usr/bin/node
/*
@Author: Kęstutis Gustaitis kestutis.gustaitis@gmail.com
@Date: 2023.12.04
*/

import { clearTerminal, digitsInNumber, printTerminal } from './utils.js';

export class Board {
  constructor(dimension = 4) {
    this.dimension = dimension;
    this.size = this.dimension * this.dimension;
    this.lastIndex = this.size - 1;
    this.maxDigits = digitsInNumber(this.lastIndex);
    this.board = this.#newGameBoard();
  }

  #newGameBoard() {
    /*
    Creates new solvable, but unsolved game board with number zero
    representing blank/empty cell.
    */
    const availableValues = [];
    const gameBoard = [];
    for (let i = 0; i < this.dimension * this.dimension; i++) {
      availableValues.push(i);
    }
    for (let i = 0; i < this.dimension; i++) {
      const row = [];
      for (let j = 0; j < this.dimension; j++) {
        const value = availableValues.splice(Math.floor(Math.random() * (availableValues.length - 1)), 1);
        row.push(value[0]);
      }
      gameBoard.push(row);
    }

    /*
    const redo = this.isPuzzleSolved(gameBoard) || !isPuzzleSolvable(gameBoard, this.dimension);
    if (!redo) {
      return gameBoard;
    }
    return this.#newGameBoard();
    */
    return gameBoard;
  }

  #printSeparatingLine() {
    /*
    Prints line like:
    `+---+---+---+---+`
    */
    let line = '+';
    for (let i = 0; i < this.dimension; i++) {
      for (let j = 0; j < this.maxDigits; j++) {
        line += '-';
      }
      line += '+';  // symbol between numbers
    }
    printTerminal(line);
  }

  #printRow(boardRow) {
    let line = '|';
    boardRow.forEach((number) => {
      const numberOfAdditionalSpaces = this.maxDigits - digitsInNumber(number);
      for (let i = 0; i < numberOfAdditionalSpaces; i++) {
        line += ' ';
      }
      if (number === 0) {
        line += ' ';
      } else {
        line += number;
      }
      line += '|';
    });
    printTerminal(line);
    this.#printSeparatingLine();
  }

  printBoard() {
    /*
    Prints board in terminal.
    */
    clearTerminal();
    printTerminal('Play game by moving zero/blank cell using arrow buttons in your keyboard.\n`Esc` to terminate game.');
    this.#printSeparatingLine();
    for (let i = 0; i < this.dimension; i++) {
      this.#printRow(this.board[i]);
    }
    if (this.isPuzzleSolved(this.board)) {
      printTerminal('Congrats you have solved the puzzle :)');
      process.exit();
    }
  }

  isPuzzleSolved(board) {
    /*
    Takes two dimension array and checks if numbers are ordered in it.
    */
    for (let i = 0; i < this.dimension; i++) {
      for (let j = 0; j < this.dimension; j++) {
        if (i === this.dimension - 1 && j == this.dimension - 1) {
          continue;  // ignore last cell
        }
        if (board[i][j] !== (1 + j) + i * this.dimension) {
          return false;
        }
      }
    }
    return true;
  }

  moveUp() {
    /*
    Checks if move is possible and switches zero/blank cell with cell above it.
    Otherwise prints error.
    */
    for (let x = 0; x < this.dimension; x++) {
      for (let y = 0; y < this.dimension; y++) {
        if (this.board[x][y] === 0) {
          if (x === 0) {
            this.printBoard();
            printTerminal('Empty cell is already at the top.');
            return;
          }
          const temp = this.board[x][y];
          this.board[x][y] = this.board[x-1][y];
          this.board[x-1][y] = temp;
          this.printBoard();
          return;
        }
      }
    }
  }

  moveDown() {
    /*
    Checks if move is possible and switches zero/blank cell with cell below it.
    Otherwise prints error.
    */
    for (let x = 0; x < this.dimension; x++) {
      for (let y = 0; y < this.dimension; y++) {
        if (this.board[x][y] === 0) {
          if (x === this.dimension - 1) {
            this.printBoard();
            printTerminal('Empty cell is already at the bottom.');
            return;
          }
          const temp = this.board[x][y];
          this.board[x][y] = this.board[x+1][y];
          this.board[x+1][y] = temp;
          this.printBoard();
          return;
        }
      }
    }
  }

  moveRight() {
    /*
    Checks if move is possible and switches zero/blank cell with cell to the right of it.
    Otherwise prints error.
    */
    for (let x = 0; x < this.dimension; x++) {
      for (let y = 0; y < this.dimension; y++) {
        if (this.board[x][y] === 0) {
          if (y === this.dimension - 1) {
            this.printBoard();
            printTerminal('Empty cell is already at the very right of the board.');
            return;
          }
          const temp = this.board[x][y];
          this.board[x][y] = this.board[x][y+1];
          this.board[x][y+1] = temp;
          this.printBoard();
          return;
        }
      }
    }
  }

  moveLeft() {
    /*
    Checks if move is possible and switches zero/blank cell with cell to the left of it.
    Otherwise prints error.
    */
    for (let x = 0; x < this.dimension; x++) {
      for (let y = 0; y < this.dimension; y++) {
        if (this.board[x][y] === 0) {
          if (y === 0) {
            this.printBoard();
            printTerminal('Empty cell is already at the very left of the board.');
            return;
          }
          const temp = this.board[x][y];
          this.board[x][y] = this.board[x][y-1];
          this.board[x][y-1] = temp;
          this.printBoard();
          return;
        }
      }
    }
  }
}
