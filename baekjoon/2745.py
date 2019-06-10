n, b = input().split()
b = int(b)
answer = 0
for i in range(len(n)):
  temp = 0
  if 'A' <= n[i]:
    temp = ord(n[i]) - 55
  else :
    temp = int(n[i])

  answer += pow(b, len(n)-1-i) * temp

print(answer)
