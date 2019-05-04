n = int(input())
arr = list(map(int, input().split()))
dp = [0] * n
dp[0] = 1
for i in range(1, n):
    max_num = 0
    for j in range(0, i):
        if(arr[j] > arr[i]):
            max_num = max(max_num, dp[j])
    
    dp[i] = max_num+1

print(max(dp))


