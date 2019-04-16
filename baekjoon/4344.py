for _ in range(0, int(input())) :
    arr = list(map(int, input().split()))
    case_num = arr.pop(0)
    avg = sum(arr) / case_num
    filter_num = len(list(filter(lambda x : x > avg, arr)))
    print("%0.3f" %(filter_num / case_num * 100), end="%\n")

