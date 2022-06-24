function solution(id_list, report, k) {
    const recordReporter = Array.from(Array(id_list.length), () => Array(id_list.length).fill(0));
    let recordReported = Array(id_list.length).fill(0);

    let idReporter, idReported;
    let indexReporter, indexReported;
    let tempReporter;

    let answer = Array(id_list.length).fill(0);

    for(let i=0; i<report.length; i++) {

        [idReporter, idReported] = report[i].split(' ');

        indexReporter = id_list.indexOf(idReporter);
        indexReported = id_list.indexOf(idReported);

        if(recordReporter[indexReporter][indexReported] === 0) {
            recordReporter[indexReporter][indexReported] = 1;
            recordReported[indexReported] += 1;
        }
    }

    for(let i=0; i<id_list.length; i++) {
        tempReporter = recordReporter[i];
        for(let j=0; j<id_list.length; j++) {
            if (recordReported[j] >= k && tempReporter[j] === 1) {
                answer[i] += 1;
            }
        }
    }
    return answer;
}