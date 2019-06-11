const {
  max
} = Math
const solution = (cookie) => {
  let answer = 0
  let len = cookie.length
  if (len == 1) {
    return 0
  }
  for (let i = 0; i < len - 1; i++) {
    let l = i
    let m = i + 1
    let cookie1 = cookie[l]
    let cookie2 = cookie[m]
    let flag = true
    if (cookie1 == cookie2) {
      answer = max(cookie1, answer)
    }
    while (flag) {
      if (l > 0 && cookie1 <= cookie2) {
        l--
        cookie1 += cookie[l]
      } else if (m < len - 1 && cookie1 >= cookie2) {
        m++
        cookie2 += cookie[m]
      } else {
        flag = false
      }
      if (cookie1 == cookie2) {
        answer = max(answer, cookie1)
      }
    }
  }

  return answer
}
