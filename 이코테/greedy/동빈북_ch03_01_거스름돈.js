function solution(n) {
    let current = n;
    let count = 0;
    while(current>0) {
        if(current>=500) {
            count += parseInt(current/500);
            current = current%500;
        } else if(current>=100) {
            count += parseInt(current/100);
            current = current%100;
        } else if(current>=50) {
            count += parseInt(current/50);
            current = current%50;
        } else if(current>=10) {
            count += parseInt(current/10);
            current = current%10;
        }
    }
    let answer = count;
    return answer;
}