function solution(participant, completion) {
    let answer = '';
    const obj = {}

    for (const a of participant) {
        if (obj[a] === undefined) obj[a] = 0
        obj[a]++
    }

    for (const a of completion) {
        obj[a]--;
    }
    answer = Object.entries(obj).filter(([k, v]) => v > 0).map(([k, v]) => k)

    return answer.join("");
}
console.log(
    solution(["leo", "kiki", "eden"], ["eden", "kiki"])

)