n, b = map(int, input().split())
stack = []

def f(su) :
  if su >= 10:
    su = chr(su+55)
  return str(su)

while n >= b:
  stack.append(f(n%b))
  n = n // b
stack.append(f(n))

stack.reverse()

print("".join(stack))

