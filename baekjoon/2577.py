a = int(input())
b = int(input())
c = int(input())

mul = str(a * b * c)
arr = [0]*10

for i in range(0, 10) :
    arr[i] = mul.count(str(i))

for el in arr :
    print(el)