import sys
import math
from collections import deque

input = sys.stdin.readline

dx = [1,0,-1,0]
dy = [0,1,0,-1]

n,L,R = map(int, input().split())

country = []
a_list = []
for i in range(n):
    country.append(list(map(int,input().split())))


def bfs(i,j):
    q = deque()
    q.append((i,j))
    visited[i][j] = True
    union = [(i,j)]
    count = country[i][j]
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny < 0 or nx >= n or ny >= n:
                continue
            if visited[nx][ny]:
                continue
            if L <= abs(country[nx][ny] - country[x][y]) <= R:
                union.append((nx,ny))
                visited[nx][ny] = True
                q.append((nx,ny))
                count += country[nx][ny]

    for x, y in union:
        country[x][y] = math.floor(count / len(union))

    return len(union)

answer = 0
while True:
    visited = [[False]*n for _ in range(n)]
    flag = False
    for i in range(n):
        for j in range(n):
            if not visited[i][j]:
                if bfs(i, j) > 1:
                    flag = True
    if not flag:
        break
    answer += 1

print(answer)
