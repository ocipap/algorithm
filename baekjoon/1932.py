n = int(input())
arr = []
ret = 0

for i in range(0, n):
    arr.append(list(map(int, input().split())))

for i in range(1, n):
    for j in range(0, len(arr[i])):
        if j == 0 :
            arr[i][j] = arr[i-1][j] + arr[i][j]
        elif len(arr[i])-1 == j : 
            arr[i][j] = arr[i-1][j-1] + arr[i][j]            
        else :
            arr[i][j] = max(arr[i-1][j], arr[i-1][j-1]) + arr[i][j]

for i in range(1, n):
    temp = max(arr[n-1][i-1], arr[n-1][i])
    if ret < temp:
        ret = temp

print(ret)