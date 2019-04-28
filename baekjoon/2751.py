import sys

arr = []
for _ in range(int(sys.stdin.readline())):
    arr.append(int(sys.stdin.readline()))

arr = sorted(arr)

for el in arr:
    print(el)