function solution(n) {
    let answer = '',
        rmd = 0

    while(n > 0) {
        rmd = n % 3
        n = Math.floor(n / 3)
        if(rmd == 0) {
            n -= 1
            rmd = 4
        }
        answer = String(rmd) + String(answer)
    }

    return answer;
}