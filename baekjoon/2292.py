n = int(input())
room = 1
add_count = 0
number_count = 0

if n == 1:
    print(1)
else :
    while(True):
        if(number_count < n-1):
            add_count = add_count + 6
            number_count = number_count + add_count
            room += 1
        else :
            print(room)
            break