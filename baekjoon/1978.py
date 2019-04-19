arr = [2]
count = 0
for i in range(3, 1001):
    flag = True
    for el in arr:
        if i %  el == 0 :
            flag = False
            break
    if flag :
        arr.append(i)
num = int(input())
nums = map(int, input().split())
for el in nums :
    if el in arr :
        count += 1

print(count)