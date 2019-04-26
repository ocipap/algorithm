# 조합 nCr 을 이용해서 푸는것

for _ in range(0, int(input())):
    r, n = map(int, input().split())
    arr = [[0] * (n+2) for i in range(n+2)]

    arr[1][1] = 1
    for i in range(2, n+2):
        for j in range(1, i+1):
            arr[i][j] = arr[i-1][j] + arr[i-1][j-1]
    
    print(arr[n+1][r+1])