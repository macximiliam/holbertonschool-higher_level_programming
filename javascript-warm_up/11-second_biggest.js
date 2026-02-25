#!/usr/bin/node

const args = process.argv.slice(2).map(x => parseInt(x));

if (args.length < 2) {
  console.log(0);
} else {
  let max = Number.MIN_SAFE_INTEGER;
  let second = Number.MIN_SAFE_INTEGER;

  for (const num of args) {
    if (num > max) {
      second = max;
      max = num;
    } else if (num > second && num < max) {
      second = num;
    }
  }
  console.log(second);
}
