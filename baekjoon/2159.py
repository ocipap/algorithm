n = int(input())
arr = [0] * (n+1)
dp = [0] * (n+1)
for i in range(1, n+1):
    arr[i] = int(input())

for i in range(1, n+1):
    if i == 1 :
        dp[i] = arr[i]
    elif i == 2:
        dp[i] = arr[i-1] + arr[i]
    else :
        dp[i] = max(max(dp[i-2]  + arr[i], dp[i-3] + arr[i-1] + arr[i]), dp[i-4] + arr[i-1] + arr[i])

print(max(max(dp[n], dp[n-1]), dp[n-2]))
