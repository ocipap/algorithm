arr = []

def push(x) :
    arr.append(x)

def pop() :
    if len(arr) == 0 :
        return -1
    return arr.pop()

def size() :
    return len(arr)

def empty() :
    if len(arr) == 0:
        return 1
    return 0

def top() :
    if len(arr) == 0 :
        return -1
    return arr[len(arr) - 1]

for _ in range(0, int(input())):
    s = input()
    if "push" in s:
        push(s.split()[1])
    elif "pop" in s:
        print(pop())
    elif "size" in s:
        print(size())
    elif "empty" in s:
        print(empty())
    elif "top" in s:
        print(top())