time = int(input())

a, b, c = 0, 0, 0

if not time % 10 == 0 :
    print(-1)
else :
    a = int(time / 300)
    b = int((time - a * 300) / 60)
    c = int((time - a * 300 - b * 60) / 10)
    print(a,b,c)
