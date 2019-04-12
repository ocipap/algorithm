a,b,c = map(int, input().split())

if a == b and a == c and b == c :
    print(a * 1000 + 10000)
elif a == b or a == c :
    print(a * 100 + 1000)
elif c == b :
    print(b * 100 + 1000)
else :
    max_num = max([a, b, c])
    print(max_num * 100)

