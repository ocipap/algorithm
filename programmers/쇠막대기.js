const solution = (arrangement) => {
    let answer = 0
    let stick = []
    arrangement = arrangement.replace(/\(\)/g, "l").split('')
    arrangement.forEach((el, i) => {
        if (el === "(") {
            stick.push(1)
        } else if (el === ")") {
            answer += stick.pop()
        } else {
            stick = stick.map(v => v + 1)
        }
    })
    return answer;
}

console.log(solution("()(((()())(())()))(())"))