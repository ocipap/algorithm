def solution(land):
  n = len(land)
  land1 = [0] * (n + 1)
  land2 = [0] * (n + 1)
  land3 = [0] * (n + 1)
  land4 = [0] * (n + 1)

  for i in range(1, n + 1):
    if i == 0:
      land1[i] = land[i-1][0]
      land2[i] = land[i-1][1]
      land3[i] = land[i-1][2]
      land4[i] = land[i-1][3]
    else :
      land1[i] = max(land2[i-1], land3[i-1], land4[i-1]) + land[i-1][0]
      land2[i] = max(land1[i-1], land3[i-1], land4[i-1]) + land[i-1][1]
      land3[i] = max(land2[i-1], land1[i-1], land4[i-1]) + land[i-1][2]
      land4[i] = max(land2[i-1], land3[i-1], land1[i-1]) + land[i-1][3]
  return max(land1[n], land2[n], land3[n], land4[n])

print(solution([[1,2,3,5],[5,6,7,8],[4,3,2,1]]))