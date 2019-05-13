const solution = heights => {
    let answer = [];
    const top = heights.map((el, i) => {
        return {
            value: el,
            index: i + 1
        }
    })
    const leng = top.length
    for(let i = 0; i < leng; i++) {
        let temp = 0
        for(let j = i-1; j >= 0 ; j--){
            if(top[i]["value"] < top[j]["value"] && temp === 0){
                temp = top[j]["index"]
            }
        }
        answer.push(temp)
    }
    return answer;
}