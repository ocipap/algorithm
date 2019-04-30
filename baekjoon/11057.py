n = int(input())
dp = [[0] * 10 for i in range(n+1) ]

for i in range(0, 10):
    dp[1][i] = 1

for i in range(2, n+1):
    for j in range(0, 10):
        for k in range(0, j+1):
            dp[i][j] += dp[i-1][k]
            dp[i][j] %= 10007

print(sum(dp[n]) % 10007)