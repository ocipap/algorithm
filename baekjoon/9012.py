for _ in range(0, int(input())):
    str = input()
    stack = []
    for el in str:
        if el == "(":
            stack.append(el)
        else :
            if len(stack) == 0:
                stack.append(":P")
                break
            else :
                stack.pop()

    if len(stack) :
        print("NO")
    else :
        print("YES")
