arr = list(map(int, input().split()))
flag = "ascending"
for i in range(0, 7):
    if arr[i] + 1 == arr[i + 1] and arr[0] == 1:
        flag = "ascending"
        continue
    elif arr[i] - 1 == arr[i + 1] and arr[0] == 8:
        flag = "descending"
        continue
    else :
        flag = "mixed"
        break

print(flag)