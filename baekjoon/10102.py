num = int(input())
arr = list(input())
aCount = 0
bCount = 0
for i in arr :
    if i == "A" :
        aCount = aCount + 1
    else  :
        bCount = bCount + 1

if aCount > bCount :
    print("A")
elif aCount < bCount :
    print("B")
else :
    print("Tie")