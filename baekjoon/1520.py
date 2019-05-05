import sys

sys.setrecursionlimit(1000000)

n, m = map(int , input().split())
arr = []
dp = [[-1] * m for i in range(n)]
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
for i in range(n):
    arr.append(list(map(int, input().split())))

def check(x, y):
    if x < 0 or x >= n or y < 0 or y >= m:
        return False
    return True

def dfs(x, y):
    if x == 0 and y == 0:
        return 1
    if not dp[x][y] == -1:
        return dp[x][y]
    dp[x][y] = 0
    for i in range(4):
        nx = dx[i]+x
        ny = dy[i]+y
        if check(nx, ny) and arr[x][y] < arr[nx][ny]:
            dp[x][y] += dfs(nx, ny)
    return dp[x][y]

print(dfs(n-1, m-1))

