arr = []
for a in range(0, int(input())):
    arr.append(input().split())

for b in arr:
    num = float(b.pop(0))
    for i in b : 
        if i == '@':
            num *= 3
        elif i == '%':
            num += 5
        else :
            num -= 7
    print("%0.2f" % num)