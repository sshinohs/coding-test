const N = 4;
const M = 10;
const ddeok = [19, 15, 10, 17];

let start = 0;
let end = Math.max(...ddeok);

// arr, target, start, end


let cut_length = start;

function binarySearch(arr, target, start, end, cut_length) {
    let mid = Math.ceil((end-start)/2+start);
    let dl = ddeok_length(arr, mid);

    if(start>end) {
        return cut_length;
    }
    if(target === dl) {
        return mid;
    } else if(target < dl) {
        return binarySearch(arr, target, mid+1, end, mid);
    } else if(target > dl) {
        return binarySearch(arr, target, start, mid-1, mid-1);
    }
}


function ddeok_length(arr, cut_length) {
    let sum = 0;
    arr.forEach((value, index, array) => {
        let remained = value - cut_length;
        if (remained>0) {
            sum += remained;
        }
    })
    return sum;
}

let answer = binarySearch(ddeok, M, start, end, cut_length);

console.log(answer);