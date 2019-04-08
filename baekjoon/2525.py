a , b = map(int, input().split(" "))
time = int(input())

hour = int(time / 60)
minute = time % 60
hour = hour + int((b+minute) / 60)

print((a+hour)%24, (b+minute)%60)
