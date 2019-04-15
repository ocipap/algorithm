i = int(input())
arr = list(map(int, input().split()))
max_num = max(arr)

max_sum = sum(list(map(lambda x: x / max_num * 100, arr)))

print(max_sum / i)
