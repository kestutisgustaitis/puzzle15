#!/usr/bin/env python3
"""
@Author: Kęstutis Gustaitis kestutis.gustaitis@gmail.com
@Date: 2023.11.30

This is implementation of 15 puzzle game https://en.wikipedia.org/wiki/15_Puzzle
Program uses keyboard module, that could be installed by running:

$ python -m pip install pynput

Run game in terminal:

$ python game.py -d <dimension>
"""

from board import Board
from pynput import keyboard
from pynput.keyboard import Key
import sys, getopt


def info():
    print('python game.py -d <dimension>')
    sys.exit()

def get_dimension(arg):
    try:
        dimension = int(arg)
        if dimension < 2:
            print('dimension value has to be more or equal to 2')
            info()
        return dimension
    except:
        print('dimension value should be positive integer equal to 2 or higher')
        info()

def main(argv):
    dimension = 4
    opts, args = getopt.getopt(argv, 'hd:', ['dimension='])
    for opt, arg in opts:
        if opt == '-h':
            info()
        elif opt in ('-d', '--dimension'):
            dimension = get_dimension(arg)
    
    board = Board(dimension)
    
    def on_key_release(key):
        if key == Key.right:
            board.move_right()
        elif key == Key.left:
            board.move_left()
        elif key == Key.up:
            board.move_up()
        elif key == Key.down:
            board.move_down()
        elif key == Key.esc:
            listener.stop()
            sys.exit()

    with keyboard.Listener(on_release=on_key_release) as listener:
        listener.join()

    try:
        board.print()
    except:
        pass

if __name__ == '__main__':
    main(sys.argv[1:])
