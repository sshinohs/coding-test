
const N = 5;    // 회사의 개수
const M = 7;    // 경로의 개수

const routes = [[1, 2], [1, 3], [1, 4], [2, 4], [3, 4], [3, 5], [4, 5]];

const X = 4;    // 최종 목적
const K = 5;    // 경유지

// 찾아야 할 것: 

const INF = 1e9;

const arr = Array.from(Array(N), () => Array(N).fill(INF));

for (let i = 0; i < N; i++ ) {
    arr[i][i] = 0;
}

routes.forEach((value, index, array) => {
    arr[value[0]-1][value[1]-1] = 1;
    arr[value[1]-1][value[0]-1] = 1;
});

for(let i=0; i<N; i++) {
    for(let j=0; j<N; j++) {
        for(let k=0; k<N; k++) {
            if(arr[j][i]!==INF && arr[i][k]!==INF) {
                if(arr[j][k] > arr[j][i]+arr[i][k]) {
                    arr[j][k] = arr[j][i]+arr[i][k];
                }
            }
        }
    }
    // console.log(i);
    // console.log(arr);
}

const answer = arr[1-1][K-1]+arr[K-1][X-1];

console.log(answer);