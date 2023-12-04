#!/usr/bin/node
/*
@Author: Kęstutis Gustaitis kestutis.gustaitis@gmail.com
@Date: 2023.12.04

This is implementation of 15 puzzle game https://en.wikipedia.org/wiki/15_Puzzle

Run game in terminal:

$ node game.js -d <dimension>
*/

import readline from 'readline';
// import yargs from 'yargs/yargs'; 
import { Board } from './board.js'; 


/*
const options = yargs
 .usage("Usage: -d <dimension>")
 .option("d", { alias: "dimension", describe: "Board size/dimension", type: "number", demandOption: false })
 .argv;
*/

const board = new Board();
board.printBoard();

readline.emitKeypressEvents(process.stdin);
if (process.stdin.isTTY)
    process.stdin.setRawMode(true);

process.stdin.on('keypress', (_, key) => {
  if (!key) {
    return;
  }
  if (['q', 'escape'].includes(key.name)) {
    process.exit();
  } else if (['up', 'w'].includes(key.name)) {
    board.moveUp();
  } else if (['down', 's'].includes(key.name)) {
    board.moveDown();
  } else if (['left', 'a'].includes(key.name)) {
    board.moveLeft();
  } else if (['right', 'd'].includes(key.name)) {
    board.moveRight();
  }
});
