arr = []
for a in range(0, int(input())):
    arr.append(input().split())

for el in arr :
    num = int(el[0])
    string = str(el[1])

    res = ""
    for i in range(0, len(string)) :
        res += string[i] * num

    print(res)