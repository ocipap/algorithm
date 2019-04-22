n = int(input())
memo = [0] * 46
memo[0] = 0
memo[1] = 1
for i in range(2, n+1):
    memo[i] = memo[i-1] + memo[i-2]

print(memo[n])