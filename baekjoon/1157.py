s = input()
s = s.upper()
count = {}
answer = ''
max_num = 0
flag = False


for i in range(0, len(s)):
    n = ord(s[i])
    if not n in count:
        count[n] = 0
    count[n]+=1

for el in count.keys():
    if max_num < count[el]:
        max_num = count[el]
        answer = el
        flag = False
    elif max_num == count[el]:
        flag = True


if flag == True:
    print("?")
else :
    print(chr(answer))


