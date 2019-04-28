dp = [0] * 101
dp[0] = 0
dp[1] = 1
dp[2] = 1

for i in range(3, 101):
    dp[i] = dp[i-2] + dp[i-3]

n = int(input())
for _ in range(n):
    print(dp[int(input())])
