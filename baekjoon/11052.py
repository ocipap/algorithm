n = int(input())
arr = [0] + list(map(int, input().split()))
dp =  [0] * (n+1)

for i in range(1, n+1):
    max_dp = 0
    for j in range(0, i):
        max_dp = max(max_dp, dp[j] + arr[i-j])
    dp[i] = max_dp

print(dp[n])
