def under30(a) : 
    if a < 40 :
        a = 40
    return a

arr = []
for i in range(0, 5) :
    arr.append(int(input()))

arr = list(map(under30, arr))

print(int(sum(arr) / 5))

