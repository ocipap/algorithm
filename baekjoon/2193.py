n = int(input())
dp = [0] * 91
flag = [0] * 91

dp[1] = 1
dp[2] = 1
flag[1] = 1
flag[2] = 0
for i in range(3, n+1):
    dp[i] = 2 * dp[i-1] - flag[i-1]
    flag[i] = dp[i-1] - flag[i-1]

print(dp[n])