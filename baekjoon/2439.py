num = int(input())

for i in range(1, num+1) :
    str = " " * (num - i) +  "*" * i
    print(str)