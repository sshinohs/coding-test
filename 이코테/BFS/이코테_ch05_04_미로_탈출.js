let a = [];

const N = 5;
const M = 6;

a.push([1,0,1,0,1,0]);
a.push([1,1,1,1,1,1]);
a.push([0,0,0,0,0,1]);
a.push([1,1,1,1,1,1]);
a.push([1,1,1,1,1,1]);

console.log(a);

BFS(a, [0,0]);

function BFS(a, current) {
    let count = 1;
    let i = current[0];
    let j = current[1];
    let queue = [];
    a[i][j] = 1;

    if(j-1>=0) {
        if(a[i][j-1]===1) {
            a[i][j-1] += a[i][j];
            queue.push([i, j-1]);
        }
    }

    if(i-1>=0){
        if(a[i-1][j]===1) {
            a[i-1][j] += a[i][j];
            queue.push([i-1, j]);
        }
    }

    if(i+1<N) {
        if(a[i+1][j]===1) {
            a[i+1][j] += a[i][j];
            queue.push([i+1, j]);
        }
    }

    if(j+1<M) {
        if(a[i][j+1]===1) {
            a[i][j+1] += a[i][j];
            queue.push([i, j+1]);
        }
    }

    while(queue.length!==0) {
        i = queue[0][0];
        j = queue[0][1];
        queue.shift();
        count += 1;

        if(j-1>=0) {
            if(a[i][j-1]===1) {
                a[i][j-1] += a[i][j];
                queue.push([i, j-1]);
            }
        }

        if(i-1>=0){
            if(a[i-1][j]===1) {
                a[i-1][j] += a[i][j];
                queue.push([i-1, j]);
            }
        }

        if(i+1<N) {
            if(a[i+1][j]===1) {
                a[i+1][j] += a[i][j];
                queue.push([i+1, j]);
            }
        }

        if(j+1<M) {
            if(a[i][j+1]===1) {
                a[i][j+1] += a[i][j];
                queue.push([i, j+1]);
            }
        }
    }
}

console.log('Answer: ', a[N-1][M-1]);