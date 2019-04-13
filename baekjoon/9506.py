while True:
    a = int(input())
    arr = []
    sumAll = 0
    if a == -1 :
        break
    for i in range(1, a ):
        if a % i == 0 :
            arr.append(i)
    sumAll = sum(arr)
    temp = " + ".join(list(map(str,arr)))
    if sumAll == a :
        print('%d = %s' %(a, temp))
    else :
        print('%d is NOT perfect.' %(a))