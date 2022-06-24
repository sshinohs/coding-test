// 경로 압축을 수행하지 않은 서로소 집합 알고리즘

const N = 7;

const execute = [[0,1,3],[1,1,7],[0,7,6],[1,7,1],[0,3,7],[0,4,2],[0,1,1],[1,1,1]];

const M = execute.length;

const arr = Array(N+1).fill(0);

arr.forEach((value, index, array) => {
    arr[index] = index;
})

execute.forEach((value, index, array) => {
    if(value[0]===0) {
        if(value[1]>=value[2]) {
            arr[value[2]] = value[1];
        } else {
            arr[value[1]] = value[2];
        }

    } else if(value[0] === 1) {
        let a_root = arr[value[1]];
        while(a_root !== arr[a_root]) {
            a_root = arr[a_root];
        }
        let b_root = arr[value[2]];
        while(b_root !== arr[b_root]) {
            b_root = arr[b_root];
        }
        if(a_root===b_root) {
            console.log('YES');
        } else {
            console.log('NO');
        }
    }
})