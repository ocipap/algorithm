n = int(input())
answer1 = list(map(int, input().split()))
answer2 = list(reversed(answer1))
dp1 = [0] * n
dp2 = [0] * n

correct = [0] * n

for i in range(0, n):
  cur1 = answer1[i]
  cur2 = answer2[i]

  for j in range(0, i):
    if answer1[j] < cur1:
      dp1[i] = max(dp1[i], dp1[j])
    
    if answer2[j] < cur2:
      dp2[i] = max(dp2[i], dp2[j])
  dp1[i] += 1
  dp2[i] += 1

for i in range(0, n):
  correct[i] = dp1[i] + dp2[n-i-1] - 1

print(max(correct))
