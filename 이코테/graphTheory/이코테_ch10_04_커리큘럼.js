// 위상 정렬 어거지

// 다수, 동시에 들을 수 있는 선행 과목이 있을 경우 틀림

const curriculum = [[10,-1],[10,1,-1],[4,1,6,-1],[4,3,2,1,-1],[3,3,-1],[12,-1]];

const N = curriculum.length;

const arr = Array(N);

const lec_time = Array(N);

const check = Array(N).fill(0);

const couple = [];

curriculum.forEach((value, index, array) => {
    arr[index] = value;
    let arr_temp = Array(N).fill(0);
    arr_temp[index] = value[0];
    lec_time[index] = arr_temp;
})


let couple_count = 0;
let check_count = 0;

while(check_count<N) {

    let cur_index_queue = [];
    let temp_couple = [];

    for(let j=0; j<N; j++) {
        if(arr[j].length === 2 && check[j] === 0) {
            cur_index_queue.push(j);
            temp_couple.push(j);
            check[j] = 1;
            check_count += 1;
        }
    }

    couple.push(temp_couple);

    while(cur_index_queue.length!==0) {
        cur_index = cur_index_queue[0];
        cur_index_queue.shift();
        
        arr.forEach((value, index, array) => {
            // console.log(value);
            let j = 1;
            while(value[j]!==-1) {
                if(value[j]===cur_index+1) {
                    arr[index].splice(j,1);
                    lec_time[cur_index].forEach((value, j) => {
                        if(lec_time[index][j]<value) {
                            lec_time[index][j] = value;
                        }
                    })
                    break;
                }
                j += 1;
            }
        })
    }

}

console.log('어거지 전', lec_time);

couple.forEach((val_c,idx_c,arr_c) => {
    if(val_c.length>1) {
        lec_time.forEach((val_l, idx_l, arr_l) => {
            let val_max = 0;
            let val_max_idx;
            val_c.forEach((val_ce, idx_ce, arr_ce) => {
                if(val_max<val_l[val_ce]) {
                    val_max = val_l[val_ce];
                    val_max_idx = val_ce;
                }
            })
            val_c.forEach((val_ce, idx_ce, arr_ce) => {
                if(val_ce !== val_max_idx) {
                    lec_time[idx_l][val_ce] = 0;
                }
            })
        })
    }
})

console.log('어거지 후',lec_time);


let answer = Array(N).fill(0);
lec_time.forEach((value, index, array) => {
    answer[index] = value.reduce((acc, cur, i) => {
        return acc + cur;
    })
})
console.log('couple: ', couple);
console.log('Answer: ', answer);