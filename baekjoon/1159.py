dic = {}
str = ""

for _ in range(0 , int(input())) :
    name = input()[0]
    if not name in dic :
        dic[name] = 1
    else :
        dic[name] += 1

for k in dic.keys():
    if dic[k] > 4 :
        str = str + k
    else : 
        continue
if len(str) == 0 :
    print("PREDAJA")
else:
    print("".join(sorted(str)))