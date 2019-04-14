num = int(input())

for i in range(0, num) :
    str = " " * i + "*" * (num - i)
    print(str)