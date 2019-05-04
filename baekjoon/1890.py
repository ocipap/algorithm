n = int(input())
arr = []
dp = [[0] * n for i in range(n)]

for i in range(n):
    arr.append(list(map(int, input().split())))
dp[0][0] = 1
for i in range(n):
    for j in range(n):
        jump = arr[i][j]
        if(jump == 0):
            continue
        if jump+i <  n:
            dp[i + jump][j] += dp[i][j]
        if jump+j <  n:
            dp[i][j + jump] += dp[i][j]

print(dp[n-1][n-1])

