def gcd(a, b) :
    if a % b == 0:
        return b
    else :
        return gcd(b, a % b)

num1, num2 = map(int, input().split())
gcd_num = gcd(num1, num2)
print(gcd_num)
print(int( num1 * num2 / gcd_num))

