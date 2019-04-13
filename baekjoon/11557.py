for _ in range(0, int(input())) :
    school = ""
    max_num = 0
    for _ in range(0, int(input())) :
        s, n = input().split()
        if max_num < int(n):
            max_num = int(n)
            school = s

    print(school)