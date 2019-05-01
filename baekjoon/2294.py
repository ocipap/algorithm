n, k = map(int, input().split())
dp = [0] * (k+1)
answer = []
for _ in range(n):
    answer.append(int(input()))
for i in range(1, k+1):
    min_num = -2
    for el in answer:
        if i >= el:
            if min_num == -2 or min_num > dp[i-el]:
                if dp[i-el] != -1:
                    min_num = dp[i-el] 
    dp[i] = min_num+1

if dp[k] == 0 :
    print(-1)
else :
    print(dp[k])