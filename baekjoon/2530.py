h, m, s = map(int, input().split())
time = int(input())

time = h * 3600 + m * 60 + s + time

h = int(time / 3600) % 24
m = int((time % 3600) / 60) % 60
s = (time % 3600) % 60

print(h, m, s)