const readline = require('readline');

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout,
});

let count = 0;
let input_arr = [];
rl.on('line', function(input) {
    input_arr[count] = input;
    count += 1;
    if (count === 2) {
        solution(input_arr);
        rl.close();
    }
});

// const a = 5;
// const b = 'R R R U D D';

function solution(input_arr) {
    const a = input_arr[0];
    const b = input_arr[1];

    let c = b.split(' ');

    let position = [1, 1];

    c.forEach((value, index, array)=>{
        if(value === 'L' && (position[1]-1)!==0) {
            position[1] -= 1;
        } else if(value ==='R' && (position[1]+1) !==a) {
            position[1] += 1;
        } else if(value === 'U' && (position[0]-1) !==0) {
            position[0] -= 1;
        } else if(value === 'D' && (position[0]+1) !==a) {
            position[0] += 1;
        }
    })
    console.log(position);
}

