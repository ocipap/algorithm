num = int(input())
count = 0
for _ in range(0, num) :
    if int(input()) == 1 :
        count = count + 1

if num / 2 < count :
    print("Junhee is cute!")
else :
    print("Junhee is not cute!")