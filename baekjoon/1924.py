arr = [31, 28, 31, 30, 31, 30, 31,31,30,31,30,31]
month = ["MON", "TUE", "WED", "THU", "FRI", "SAT", "SUN"]
answer = ""
day = 0

m, d = map(int, input().split())

for i in range(0, m - 1 ) :
    day = day + arr[i]

day  = day + d

print(month[day % 7 - 1])
