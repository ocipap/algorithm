for i in range(0, int(input())) :
    arr = list(input())
    answer = [0] * len(arr)
    for j in range(0, len(arr)): 
        if arr[j] == "X" :
            answer[j] = 0
        elif j == 0 :
            answer[j] = 1
        else :
            answer[j] = int(answer[j - 1]) + 1
    print(sum(answer))