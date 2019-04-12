x = []
y = []

def findOneElement (arr):
    if arr[0] == arr[1] :
        return arr[2]
    elif arr[1] == arr[2]:
        return arr[0]
    else :
        return arr[1]

for i in range(0, 3) :
    a, b = map(int, input().split())
    x.append(a)
    y.append(b)

answer_x = findOneElement(x)
answer_y = findOneElement(y)

print(answer_x, answer_y)


