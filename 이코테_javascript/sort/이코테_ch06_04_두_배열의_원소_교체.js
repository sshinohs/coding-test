const k = 3;
const A = [1,2,5,4,3];
const B = [5,5,6,6,5];


let count = 0;
let temp;
let idx_A, idx_B;

while(count < k) {
    count += 1;
    idx_A = A.indexOf(Math.min(...A));
    idx_B = B.indexOf(Math.max(...B));

    if(A[idx_A] >= B[idx_B]) break;

    temp = A[idx_A];
    A[idx_A] = B[idx_B];
    B[idx_B] = temp;
}

const result = A.reduce(function add(sum, curVal) {
    return sum + curVal;
})

console.log(A);
console.log(B);

console.log(result);