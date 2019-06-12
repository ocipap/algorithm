const solution = (A, B) => {
  let result = 0
  let i = 0
  let j = 0
  A = A.sort((a, b) => a - b)
  B = B.sort((a, b) => a - b)

  while (j < B.length) {
    if (A[i] < B[j]) {
      result++
      i++
      j++
    } else {
      j++
    }
  }
  return result
}

console.log(
  solution([1,1,1,1], [2,2,2,2]),
  solution([5,1,3,7],	[2,2,6,8])
)