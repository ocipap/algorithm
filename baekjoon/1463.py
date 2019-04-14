num = int(input())
dp = [0] * 1000001
dp[0] = 0
dp[1] = 0

case1 = 0
case2 = 0
answer = 0

for i in range(2, num + 1):
    if i % 3 == 0:
        case1 = dp[i // 3] + 1
        case2 = dp[i - 1] + 1
        answer = min(case1, case2)
        dp[i] = answer
    elif i % 2 == 0:
        case1 = dp[i // 2] + 1
        case2 = dp[i - 1] + 1
        answer = min(case1, case2)
        dp[i] = answer
    else:
        answer = dp[i-1] + 1
        dp[i] = answer

print(answer)

