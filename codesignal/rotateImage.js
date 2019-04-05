function rotateImage(a) {
    let obj = {}
    let answer = []
    let leng = a.length
    
    for (let i = 0; i< leng; i++ ) {
        for(let j = 0; j < leng; j++) {
            if(!obj[j]) {obj[j] = []}
            obj[j].push(a[i][j])
        }
    }
    for(const arr in obj) {
        answer.push(obj[arr].reverse())
    } 
    return answer
}

console.log( rotateImage( [[1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]]) )
