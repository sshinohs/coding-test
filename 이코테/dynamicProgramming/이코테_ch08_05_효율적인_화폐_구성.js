const N = 3;
const M = 4;

const max_value = 10001;

const currency = [3,5,7];


const arr = Array.from({length: M+1}, () => 10001);

arr[0] = 0;


currency.forEach((value, index, array) => {
    for(let i = value; i<= M; i++) {
        if(arr[i-value] !== max_value) {
            arr[i] = arr[i-value] + 1;    
        }
    }
})

let answer;
if (arr[M] === 10001) {
    answer = -1;
} else {
    answer = arr[M];
}

console.log(answer);