arr = []
new_arr = []

n, k = map(int, input().split())
index = 0
for i in range(1, n+1):
    arr.append({"v" : i, "n" : i+1})

while len(arr) > 0 :
    index = (index + k - 1) % len(arr)
    arr[index - 1]["n"] = arr[(index + 1) % len(arr)]["n"]
    new_arr.append(str(arr.pop(index)["v"]))

print("<%s>" %(", ".join(new_arr)))