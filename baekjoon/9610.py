dic = {"Q1": 0, "Q2": 0,"Q3": 0,"Q4": 0,"AXIS": 0}

for i in range(0, int(input())) :
    a, b = map(int, input().split())
    if a == 0 or b == 0 :
        dic["AXIS"] = dic["AXIS"] + 1
    elif a < 0 and b < 0:
        dic["Q3"] = dic["Q3"] + 1
    elif a < 0 and b > 0:
        dic["Q2"] = dic["Q2"] + 1
    elif a > 0 and b < 0:
        dic["Q4"] = dic["Q4"] + 1
    else :
        dic["Q1"] = dic["Q1"] + 1

for i in dic:
    print('%s: %d' %(i, dic[i]))