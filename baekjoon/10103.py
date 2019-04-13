c, s = 100, 100

for _ in range(0, int(input())) :
    a, b = map(int, input().split())
    if a < b :
        c = c - b
    elif a > b :
        s = s - a

print(c)
print(s)