s = input()
s = s.replace("()", "l")
answer = 0
stack = []
for i in s:
  if i == "(":
    stack.append(1)
  elif i == ")":
    temp = stack.pop()
    answer += temp
  else :
    stack = list(map(lambda x: x+1, stack))

print(answer)