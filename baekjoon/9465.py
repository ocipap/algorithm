for _ in range(0, int(input())):
    n = int(input())
    arr = []    
    dp = [[0] * n for i in range(2)]
    arr.append(list(map(int, input().split())))
    arr.append(list(map(int, input().split())))
    for i in range(0, n):
        if i == 0:
            dp[0][i] = arr[0][i]
            dp[1][i] = arr[1][i]
        elif i == 1:
            dp[0][i] = dp[1][i-1] + arr[0][i]
            dp[1][i] = dp[0][i-1] + arr[1][i]
        else :
            dp[0][i] = max(dp[1][i-1], dp[1][i-2]) + arr[0][i]
            dp[1][i] = max(dp[0][i-1], dp[0][i-2]) + arr[1][i]
    print(max(dp[1][n-1], dp[0][n-1]))