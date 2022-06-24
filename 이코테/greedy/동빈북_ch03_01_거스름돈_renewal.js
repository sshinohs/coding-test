function solution(n) {
    let current = n;
    let count = 0;

    let coin = [500, 100, 50, 10];

    coin.forEach((value, index, array) => {
        if(current>=value) {
            count += parseInt(current/value);
            current = current%value;
        }
    })
    let answer = count;
    return answer;
}

console.log(solution(1260));