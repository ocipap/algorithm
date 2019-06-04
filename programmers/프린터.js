function solution(priorities, location) {
  let answer = 1
  let stack = []
  let objArr = priorities.map((el, i) => (location === i) ? { flag: true, pr: el } : { flag: false, pr: el })

  while (objArr.length) {
    let cur = objArr.shift()
    if(objArr.find(({pr}) => pr > cur.pr)){
      objArr.push(cur)
    } else if (cur.flag){
      return answer
    } else {
      answer++
    }
  }
  return answer
}