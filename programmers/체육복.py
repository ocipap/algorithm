def solution(n, lost, reserve):
    arr = [0] * (n+1)
    for i in lost:
        arr[i] -= 1
    for i in reserve:
        arr[i] += 1
    for i in range(n):
        if arr[i] == -1:
            if arr[i-1] == 1:
                arr[i] = 0
                arr[i-1] = 0
            elif arr[i+1] == 1:
                arr[i] = 0
                arr[i+1] = 0
    answer = n - arr.count(-1)
    return answer

solution(3, [3], [1])