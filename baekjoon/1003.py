dic0 = [0] * 41
dic1 = [0] * 41

dic0[0] = 1
dic0[1] = 0
dic1[0] = 0
dic1[1] = 1

for i in range(2, 41) :
    dic0[i] = dic0[i - 1] + dic0[i - 2]
    dic1[i] = dic1[i - 1] + dic1[i - 2]

for _ in range(0, int(input())):
    n = int(input())
    print(dic0[n], dic1[n])


