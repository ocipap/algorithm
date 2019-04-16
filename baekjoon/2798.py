n, m = map(int, input().split())
arr = list(map(int, input().split()))
arr = sorted(arr)
answer = arr[0] + arr[1] + arr[2]
for i in range(0, n-2):
    for j in range(i+1, n-1) :
        for k in range(j+1, n):
            hab = arr[i] + arr[j] + arr[k]
            if hab <= m and answer < hab :
                answer = hab

print(answer)
