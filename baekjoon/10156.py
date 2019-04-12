a, num, money = map(int, input().split())

if a * num < money :
    print(0)
else :
    print(a * num - money)