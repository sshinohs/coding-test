const arr1 = [3, 15, 27, 12];

arr1.sort(function (a, b) {
    if(a>b) return -1;
    if(a===b) return 0;
    if(a<b) return 1;
})

console.log(arr1);