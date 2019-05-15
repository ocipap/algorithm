const obj = {}
const solution = (clothes) => {
    let answer = 0
    let arr = []
    clothes.forEach(([name, kind]) => {
        if(obj[kind] === undefined) obj[kind] = []
        obj[kind].push(name)
    })
    for(const a in obj) {
        arr.push(obj[a].length)
    }
    answer = arr.map(v => v + 1).reduce((a, b) => a * b)
    return answer-1
}