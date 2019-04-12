point = 0

def diceGame(a, b, c) :
    if a == b and b == c :
        return a * 1000 + 10000
    elif a == b :
        return a * 100 + 1000
    elif b == c :
        return b * 100 + 1000
    elif a == c :
        return c * 100 + 1000
    else :
        return max([a, b, c]) * 100

for i in range(0, int(input())):
    a, b, c = map(int, input().split())
    point = max(diceGame(a, b, c), point)

print(point)