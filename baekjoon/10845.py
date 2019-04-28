arr = []
n = int(input())

for _ in range(n):
    inst = input().split()
    if inst[0] == "push":
        arr.append(int(inst[1]))
    elif inst[0] == "pop":
        if len(arr) == 0:
            print(-1)
        else :
            print(arr.pop(0))
    elif inst[0] == "size":
        print(len(arr))
    elif inst[0] == "empty":
        if(len(arr) == 0):
            print(1)
        else :
            print(0)
    elif inst[0] == "front":
        if(len(arr) == 0):
            print(-1)
        else :
            print(arr[0])
    elif inst[0] == "back":
        if(len(arr) == 0):
            print(-1)
        else :
            print(arr[-1])



