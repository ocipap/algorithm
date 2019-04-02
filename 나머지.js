function solution(a, b, c) {
    let answer = []
    answer = [(a + b) % c, (a % c + b % c) % c, (a* b) % c, (a % c* b % c) % c]
    return answer.join("\n")
}

console.log(solution(5, 8, 4))