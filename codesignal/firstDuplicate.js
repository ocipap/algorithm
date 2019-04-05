function firstDuplicate(a) {
    let leng = a.length
    let dic = {}
    
    for(let i = 0; i < leng; i++) {
        if(dic[a[i]]) { dic[a[i]]++ }
        else { dic[a[i]] = 1 }
        if(dic[a[i]] == 2) return a[i]
    }
    return -1
}

console.log(firstDuplicate([1, 1, 2, 2, 1]))