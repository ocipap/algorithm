function solution(a, b) {
    var answer = 0;
    let {
        i,
        l
    } = bs(a, b);
    if (!l) {
        return i;
    } else {
        for (let a = i; a <= l; a++) {
            answer += a;
        }
        return answer;
    }
}

function bs(a, b) {
    if (a === b) {
        return {
            i: a
        };
    };
    return a > b ? {
        i: b,
        l: a
    } : {
        i: a,
        l: b
    };
}