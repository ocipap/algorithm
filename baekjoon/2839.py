num = int(input())
answer = -1

for i in range(0, num // 3 + 1) :
    if (num - (i * 3)) % 5 == 0 :
        answer = i + ((num - (i * 3)) // 5)
        break

print(answer)


