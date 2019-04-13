h, m = map(int, input().split())
if h == 0 :
    h = 24
time = h * 60 + m
time = time - 45

h = int(time / 60) % 24
m = time % 60
print(h, m)