#!/usr/bin/node
/*
@Author: Kęstutis Gustaitis kestutis.gustaitis@gmail.com
@Date: 2023.12.04
*/

export function clearTerminal() {
  console.clear();
}

export function digitsInNumber(number) {
  /*
  Returns length of digits in positive integer.
  */
  if (number === 0) {
    return 1;
  }
  return parseInt(Math.log10(number)) + 1
}

export function printTerminal(text) {
  console.log(text);
}
