const N = 7;

const routes = [[1,2,3],[1,3,2],[3,2,1],[2,5,2],[3,4,4],[7,3,6],[5,1,5],[1,6,2],[6,4,1],[6,5,3],[4,5,3],[6,7,4]];

const M  = routes.length;

const INF = 1e9;

const arr = Array(N+1).fill(0);

let cost = 0;
let highest_cost = 0;

arr.forEach((value, index, array) => {
    arr[index] = index;
})

for(let i=0; i<M; i++) {
    let min_cost_index;
    let min_value = INF;

    routes.forEach((value, index, array) => {
        if (value[2]<min_value) {
            min_value = value[2];
            min_cost_index = index;
        }
    })

    // 루트 노드가 같나?

    // console.log('min_cost_index');
    // console.log(min_cost_index);
    
    let best_routes = routes[min_cost_index];

    // console.log('best_routes: ', best_routes);
    console.log('###')
    console.log('best_routes: ', best_routes);
    console.log(find_root(arr, arr[best_routes[0]]));
    console.log(find_root(arr, arr[best_routes[1]]));
    console.log('###')
    
    if(find_root(arr, arr[best_routes[0]])!==find_root(arr, arr[best_routes[1]])) {
        console.log('통과')
        if(best_routes[0]<best_routes[1]) {
            //1 업데이트
            arr.forEach((value, index, array) => {
                if(value===arr[best_routes[1]]) {
                    arr[index] = arr[best_routes[0]];
                }
            })
        } else {
            //0 업데이트
            arr.forEach((value, index, array) => {
                if(value===arr[best_routes[0]]) {
                    arr[index] = arr[best_routes[1]];
                }
            })
        }

        // change_root(arr, best_routes[0]);
        // change_root(arr, best_routes[1]);
        cost += best_routes[2];
        if(best_routes[2]>highest_cost) {
            highest_cost = best_routes[2];
        }
    }
    routes[min_cost_index][2] = INF;
    console.log('arr');
    console.log(arr);
    console.log('==========')
}

console.log(arr);

function change_root(arr, a) {
    let current_root_index = arr[a];
    console.log('current_root_index: ', current_root_index);
    let best_root_index = a;
    
    while(arr[best_root_index] !== best_root_index) {
        best_root_index = arr[best_root_index];
    }
    console.log('best_root_index: ', best_root_index);
    arr.forEach((value, index, array) => {
        if(value==current_root_index) {
            arr[index] = best_root_index;
        }
    })
}

function find_root(arr,a) {
    root_index = a;
    while(arr[root_index] !== root_index) {
        root_index = arr[root_index];
    }
    return root_index;
}

let answer = cost - highest_cost;

console.log('Answer: ', answer);