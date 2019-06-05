function solution(progresses, speeds) {
  let temp = 0
  return progresses
    .map(el => 100 - el)
    .map((el, i) => Math.ceil(el / speeds[i]))
    .reduce((arr, el) => {
      if (temp < el) {
        arr.push(1)
        temp = el
      } else {
        arr[arr.length - 1] += 1
      }
      return arr
    }, [])
}