#!/usr/bin/node

const times = parseInt(process.argv[2]);

if (isNaN(times)) {
  console.log('Missing number of occurrences');
} else if (times > 0) {
  let i = 0;
  while (i < times) {
    console.log('C is fun');
    i++;
  }
}
