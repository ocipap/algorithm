import math

n = int(input())
dp = [0] * (n+1)
arr = []

for i in range(1, int(math.sqrt(n))+ 1):
    arr.append(i * i)

for i in range(1, n+1):
    min_num = n
    for el in arr:
        if(el <= i):
            min_num = min(min_num, dp[i - el])
    dp[i] = min_num+1

print(dp[n])

