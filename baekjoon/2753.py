a = int(input())

result = 1 if (a % 4 == 0 and a % 100 != 0) or a % 400 == 0 else 0

print(result)