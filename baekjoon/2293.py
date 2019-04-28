n, k = map(int, input().split())
dp = [0] * 10001
dp[0] = 1
for _ in range(0, n):
    su = int(input())
    for i in range(0, k+1) :
        if su <= i :
            dp[i] = dp[i] + dp[i - su]

print(dp[k])