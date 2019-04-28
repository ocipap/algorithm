n = int(input())
t = [0]
p = [0]
dp = [0] * (n+1)
for _ in range(n):
    t_val, p_val = map(int, input().split())
    t.append(t_val)
    p.append(p_val)

for i in range(1, n+1):
    if (t[i] + i > n+1):
        continue
    max_price = 0    
    for j in range(1, i):
        if j + t[j] <= i:
            max_price = max(dp[j], max_price)
    dp[i] = max_price + p[i]

print(max(dp))


