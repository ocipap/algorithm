memo = [0] * 1001
memo[0] = 1
memo[1] = 1
memo[2] = 2

n = int(input())

for i in range(3, n+1):
    memo[i] = memo[i-1] + memo[i-2]

print(memo[n] % 10007)