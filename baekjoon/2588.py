a = int(input())
b = input()
int_b = int(b)
list_b = list(b)

for i in reversed(list_b):
    print(int(i) * a)

print(a * int_b)

