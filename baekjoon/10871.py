i, num = map(int, input().split())
arr = list(map(int, input().split()))
answer = ""
for el in arr :
    if el < num :
        answer = answer + str(el) + " "
print(answer)