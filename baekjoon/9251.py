text1 = input()
text2 = input()
dp = [[-1] * (len(text1)+1) for i in range((len(text2)+1))]

def solution(i, j):
    if i >= len(text1) or j >= len(text2):
        return 0
    elif dp[i][j] != -1:
        return dp[i][j]
    else:
        if text1[i] == text2[j]:
            dp[i][j] = solution(i+1, j+1) + 1
            return dp[i][j]
        else :
            dp[i][j] = max(solution(i+1,j), solution(i, j+1), solution(i+1,j+1))
            return dp[i][j]

print(solution(0, 0))
