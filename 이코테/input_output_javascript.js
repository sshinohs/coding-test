const readline = require('readline');

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout,
});

let count = 0;

rl.on('line', function(input) {
    console.log(`Recived : ${input}`);
    count += 1;
    if (count === 3) {
        rl.close();
    }
});