a = input()

start = 0
end = 10

while True:
    print(a[start:end], end="\n")
    
    if len(a[end:]) < 11:
        print(a[end:])
        break
    else:
        start = end
        end += 10