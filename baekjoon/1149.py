n = int(input())
cost1 = [0] * (n+1)
cost2 = [0] * (n+1)
cost3 = [0] * (n+1)

for i in range(1, n+1):
    r, g, b = map(int, input().split())
    if i == 1 :
        cost1[i] = r
        cost2[i] = g
        cost3[i] = b
    else :
        cost1[i] = min(cost2[i-1], cost3[i-1] )+ r
        cost2[i] = min(cost1[i-1], cost3[i-1] )+ g
        cost3[i] = min(cost2[i-1], cost1[i-1] )+ b

print(min(min(cost1[n], cost2[n]), cost3[n]))

