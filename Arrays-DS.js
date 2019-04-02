function reverseArray(a) {
    let res = []
    let length = a.length
    for (let i = length - 1; i >= 0; i--){
        res.push(a[i])
    }
    return res
}