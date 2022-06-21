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
for(let i=0; i<N;i++) {
    let cur_node;
    let cur_index;

    let temp_couple =[];

    console.log('couple_count: ', couple_count);
    if(couple_count === 0) {
        for (let j=0; j<N; j++) {
            if(arr[j].length ===2 && check[j] ===0) {
                temp_couple.push(j);
                couple_count += 1;
            }
        }
        console.log('temp_couple: ', temp_couple);
        couple.push(temp_couple);
    }

    for(let j=0; j<N; j++) {
        if(arr[j].length ===2 && check[j] === 0) {
            cur_node = arr[j];
            cur_index = j;
            check[j] = 1;
            break;
        }
    }

    console.log('cur_index: ', cur_index);

    couple_count -= 1;

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
console.log(answer);


// lec_time.forEach((value, index, array) => {
//     couple.forEach((val_c, idx_c, arr_c) => {
//         let max_val = 0;
//         val_c.forEach((val_d, idx_d, arr_d) => {
//             if(max_val < value[val_d]) {
//                 max_val = value[val_d];
//             }
//         })
//         // console.log(max_val);
//     })
//     sum = value.reduce((acc, cur, i) => {
//         return acc + cur;
//     })
// })

// console.log(couple);
// console.log(sum);