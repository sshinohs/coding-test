const N = 10;
const food = [1, 3, 1, 5, 7, 3, 2, 10, 9, 8];

const arr = [0, food[0]];

for(let i = 2; i<=N; i++) {
    if (arr[i-2]+food[i-1]>=arr[i-1]) {
        arr[i] = arr[i-2]+food[i-1];
    } else {
        arr[i] = arr[i-1];
    }
}
console.log(arr);