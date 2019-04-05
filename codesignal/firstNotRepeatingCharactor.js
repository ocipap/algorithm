function firstNotRepeatingCharacter(s) {
    let dic = {}
    for(const a of s) {
        if(dic[a]) dic[a]++
        else dic[a] = 1
    }
    for(const a of Object.entries(dic)) {
        let [k, v] = a
        if(v == 1) return k
    }
    return "_"
}

console.log(firstNotRepeatingCharacter("abacabad"))