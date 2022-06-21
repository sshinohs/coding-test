const num_student = 7;
const data_student = [['홍길동', 95], ['이순신', 77], ['김삼순', 80], ['박탁스', 30], ['배이더', 42], ['캄프누', 10], ['킹받스', 77]];

console.log(num_student);
console.log(data_student);

data_student.sort(function (a, b) {
    if(a[1]>b[1]) return 1;
    if(a[1]===b[1]) return 0;
    if(a[1]<b[1]) return -1;
})

console.log(data_student);