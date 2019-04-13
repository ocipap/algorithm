arr = list(input())
answer = 10
now = arr[0]

for i in range(1, len(arr)) :
    if arr[i] == now :
        answer = answer + 5
    else :
        answer = answer + 10
        now = arr[i]

print(answer)