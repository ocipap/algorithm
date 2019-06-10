function solution(a, b) {
  var date = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30 ,31]
  var weekend = ["THU","FRI","SAT","SUN","MON","TUE","WED"]
  var answer = 0;
  
  for (let i = 0; i < a-1; i++){
      answer += date[i]
  }
  answer += Number(b)
  answer %= 7
  
  return weekend[answer];
}