const N = 5;
const partsInStock = [8,3,7,9,2,3,1];

const M = 3;
const partsOrdered = [5,7,9];

const arr = [1,2,3,3,7,8,9];
let start = 0;
let end = arr.length-1;


function binarySearch(arr, target, start, end) {

    if(start > end){
        return -1;
    }

    let mid = Math.ceil((end-start+1)/2-1+start);

    if (arr[mid] === target) {
        return mid;
    } else if (arr[mid] > target) {
        return binarySearch(arr, target, start, mid-1);
    } else if (arr[mid] < target) {
        return binarySearch(arr, target, mid+1, end);
    }
}

// console.log(binarySearch(arr,6,start,end))


partsOrdered.forEach((value, index, array) => {
    if(binarySearch(arr, value, start, end)>=0){
        return console.log('yes');
    } else {
        return console.log('no');
    }
    return value;
})
