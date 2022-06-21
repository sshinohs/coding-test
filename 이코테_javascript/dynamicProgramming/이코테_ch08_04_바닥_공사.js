const N = 3;

const V = 2;

const arr = [1, 1];

for(let i=2; i<=N; i++) {
    arr[i] = arr[i-2]*2+arr[i-1];
}

const answer = arr[N]%796796;
console.log(answer);