cnt = int(input())
arr = []
number = 0

for i in range(1, cnt+1):
    arr.append(input().split())
    
for [a, b] in arr:
    number += 1
    a = int(a)
    b = int(b)
    print("Case #"+str(number)+": "+str(a+b))

