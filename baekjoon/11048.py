n, m  = map(int, input().split())
dp = [[0] * (m+1) for i in range(n+1)]
answer = [[0] * (m+1)]

for _ in range(n):
    answer.append([0] + list(map(int, input().split())))

for i in range(1, n+1):
    for j in range(1, m+1):
        dp[i][j] = max(max(dp[i-1][j], dp[i][j-1]), dp[i-1][j-1]) + answer[i][j]

print(dp[n][m])