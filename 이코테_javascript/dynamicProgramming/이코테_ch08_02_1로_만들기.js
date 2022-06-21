const X = 26;

const arr = [0, 0];

for(let i = 2; i <= X; i++) {
    let value;
    count = 30000;
    // console.log(i%2);
    if(i%5 === 0) {
        value = i;
        value /= 5;
        count = arr[value] + 1;
    }
    if(i%3 === 0) {
        value = i;
        value /= 3;
        if (arr[value]+1 < count) {
            count = arr[value] + 1;
        }
    }
    if(i%2 === 0) {
        value = i;
        value /= 2;
        if (arr[value]+1 < count) {
            count = arr[value] + 1;
        }
    }
    value = i;
    value -= 1;
    if (arr[value]+1 < count) {
        count = arr[value] + 1;
    }
    arr[i] = count;
}

console.log(arr[X]);