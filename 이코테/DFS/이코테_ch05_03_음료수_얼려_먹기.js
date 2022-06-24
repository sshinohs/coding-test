let a = [];

const N = 4;
const M = 5;

a.push([0,0,1,1,0]);
a.push([0,0,0,1,1]);
a.push([1,1,1,1,1]);
a.push([0,0,0,0,0]);


function DFS(a, current) {
    let i = current[0];
    let j = current[1];
    a[i][j] = 1;

    if(i+1<N) {
        if(a[i+1][j]===0) {
            DFS(a, [i+1, j]);
        }
    }

    if(j+1<M) {
        if(a[i][j+1]===0) {
            DFS(a, [i, j+1]);
        }
    }
}

let count = 0;

for(let i=0; i<N; i++) {
    for(let j=0; j<M; j++) {
        if(a[i][j]===0){
            count += 1;
            DFS(a, [i, j]);
        }
    }
}

console.log('Count: ', count);