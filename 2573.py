import sys
from collections import deque
sys.setrecursionlimit(10**5)

input = sys.stdin.readline

n,m = map(int,input().split())
ice = []
for _ in range(n):
    ice.append(list(map(int,input().split())))
dx = [1,-1,0,0]
dy = [0,0,1,-1]
visited = [[False]*m for _ in range(n)]
t = 0

def next(ice):
    ar = deque([])

    for i in range(1,n-1):
        for j in range(1,m-1):
            if ice[i][j] != 0:
                check = [ice[i - 1][j], ice[i + 1][j], ice[i][j - 1], ice[i][j + 1]]
                ar.append(check.count(0))

    for i in range(1,n-1):
        for j in range(1,m-1):
            if ice[i][j] != 0:
                round = ar.popleft()
                ice[i][j] -= round
                if ice[i][j] < 0:
                    ice[i][j] = 0
    return ice

def dfs(x,y,visited,ice):
    visited[x][y] = True

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx <n and 0 <= ny < m and ice[nx][ny] != 0:
            if not visited[nx][ny]:
                dfs(nx,ny,visited,ice)

t = 0
while True:
    count = 0
    visited = [[False]*m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            if not visited[i][j] and ice[i][j] != 0:
                dfs(i,j,visited,ice)
                count += 1

    if count > 1:
        print(t)
        break

    else:
        t += 1
        ice = next(ice)

        if sum(map(sum,ice)) == 0:
            print(0)
            break
