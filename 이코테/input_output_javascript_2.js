const readline = require("readline");


function check_validity(input) {
    if(true) {
        return true;
    }
    return false;
}
function solution(input) {
    console.log(input);
}

const r1 = readline.createInterface({
    input: process.stdin,
    output: process.stdout,
});

r1.prompt();

r1.on("line", (input) => {
    let is_valid_input = check_validity(input);
    if (is_valid_input) {
        solution(input);
        r1.close();
    } else {
        console.log("Wrong input. Please write valid input.");
        r1.prompt();
    }
}).on("close", function () {
    process.exit();
});