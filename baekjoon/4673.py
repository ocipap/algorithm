arr = [0] * 10001

def isSelfNumber () :
    for i in range(1, 10001) :
        if arr[i] == 0 :
            print(i)
        else :
            continue

for i in range(1, 10001):
    index = i
    for s_index in range(0, len(str(i))):
        index += int(str(i)[s_index])
    if index > 10000 :
        continue
    arr[index] = 1
    
isSelfNumber()