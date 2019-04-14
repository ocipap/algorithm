s1 = input()
s2 = ""
count = 1

def solution(s) :
    temp = int(s[0]) + int(s[1])
    return s[1] + str(temp % 10)

if len(s1) == 1 :
    s1 = s1[0] + "0"

s2 = solution(s1)

while not s1 == s2 :
    s2 = solution(s2)
    count += 1

print(count)