num = int(input())
arr = list(map(int, input().split()))

start = 0
end = 0
answer = 0
check = False


for i in range(0, num - 1) :
    if arr[i] < arr[i+1] :
        start = arr[i]
        for j in range(i, num) :
            if num == j + 1 and arr[j-1] < arr[j]:
                check = False
            elif arr[j] < arr[j + 1]:
                check = True
            else :
                check = False
            if not check:
                end = arr[j]
                if end - start > answer :
                    answer = end - start
                start = 0
                end = 0
                break
            
print(answer)