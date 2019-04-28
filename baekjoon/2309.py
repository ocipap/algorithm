arr = []
answer = []
for _ in range(9):
    arr.append(int(input()))

for i in range(0, 9):
    for j in range(0, 8):
        temp_arr = list(arr)
        del temp_arr[i]
        del temp_arr[j]
        if sum(temp_arr) == 100:
            answer = sorted(temp_arr)
            break
    if 7 == len(answer):
        break

for el in answer:
    print(el)