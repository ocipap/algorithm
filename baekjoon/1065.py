answer = 0
n = int(input())

def isHansu(s) :
    s = str(s)
    if len(s) == 1 :
        return True
    flag = int(s[0]) - int(s[1])
    for i in range(1, len(s)):
        if not int(s[i-1]) - int(s[i]) == flag:
            return False
    return True


for i in range(1, n+1) :
    if isHansu(i) :
        answer += 1

print(answer)