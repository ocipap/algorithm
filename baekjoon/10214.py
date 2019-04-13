for _ in range(0, int(input())) :
    sum_y, sum_k = 0, 0
    for i in range(0, 9) :
        y, k = map(int, input().split())
        sum_y = sum_y + y
        sum_k = sum_k + k
    if sum_k < sum_y :
        print("Yonsei")
    elif sum_k > sum_y : 
        print("Korea")
    else :
        print("Draw")