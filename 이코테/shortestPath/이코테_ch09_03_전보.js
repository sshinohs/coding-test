// const N = 6;
// const M = 8;
// const C = 1;

// const routes = [[1,2,1],[1,6,4],[1,5,5],[2,5,3],[3,1,2],[3,4,5],[5,3,4],[6,3,3]];


const N = 3;
const M = 2;
const C = 1;

const routes = [[1,2,4],[1,3,2]];

// 자바스크립트는 우선순위 큐를 직접 구현해야 함..

// 일단 배열로 처리해볼 것.

const INF = 1e9;

const arr = Array(N+1).fill(INF);

arr[0] = 0;
arr[1] = 0;

const check = Array(N+1).fill(0);

check[0] = 1;

routes.forEach((value, index, array) => {
    if(value[0]===C) {
        arr[value[1]] = value[2];
    }
})
check[C] = 1;

function find_next_site(arr, check) {
    let min_value = INF;
    let min_index;
    for(let i=0; i<arr.length; i++) {
        if(check[i]!==1) {
            if(arr[i]<min_value) {
                min_value = arr[i];
                min_index = i;
            }
        }
    }
    return min_index;
}

let count = 1;

while(count<N) {
    let next_site = find_next_site(arr, check);

    // console.log('next_site: ', next_site);
    // console.log('count: ', count);

    routes.forEach((value, index, array) => {
        if(value[0]===next_site) {
            if (arr[value[1]]>arr[next_site]+value[2]) {
                arr[value[1]] = arr[next_site] + value[2];
            }
        }
    })
    check[next_site] = 1;
    count +=1;
}

let answer = Math.max(...arr);

console.log(answer);