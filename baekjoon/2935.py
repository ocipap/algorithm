import operator

ops = {"+": operator.add, "*": operator.mul}

num1 = int(input())
op = str(input())
num2 = int(input())

print(ops[op](num1, num2))


