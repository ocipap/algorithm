const solution = (n , words) => {
  let answer = [0, 0]
  let history = []
  let word = words[0]

  for(let i = 1; i < words.length; i++) {
    history.push(word)
    let cur = words[i]
    answer =  [(i % n) + 1, parseInt(i / n) + 1]
    if (word[word.length - 1] != cur[0] || history.includes(cur)) {
      return answer
    }
    word = cur
  }
  return [0,0]
}