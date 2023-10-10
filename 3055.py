import sys
from collections import deque

input = sys.stdin.readline

r, c = map(int, input().split())
graph = [list(input()) for _ in range(r)]
visited = [[False] * c for _ in range(r)]
dx = [-1,1,0,0]
dy = [0,0,-1,1]

sx, sy = 0, 0
for i in range(r):
    for j in range(c):
        if graph[i][j] == "S":
            sx, sy = i, j
            graph[i][j] = "."

def water():
    water2 = []
    for i in range(r):
        for j in range(c):
            if graph[i][j] == "*" and not visited[i][j]:
                water2.append((i, j))
                visited[i][j] = True
    for x, y in water2:
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < r and 0 <= ny < c and not visited[nx][ny]:
                if graph[nx][ny] == ".":
                    graph[nx][ny] = "*"

def bfs(x,y):
    q = deque([(x,y)])
    visited[x][y] = True
    count = 0
    while q:
        count += 1

        water()

        for _ in range(len(q)):
            x, y = q.popleft()

            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]

                if 0 <= nx < r and 0 <= ny < c and not visited[nx][ny]:
                    if graph[nx][ny] == ".":
                        q.append((nx, ny))
                        visited[nx][ny] = True
                    elif graph[nx][ny] == "D":
                        return count

    return "KAKTUS"


print(bfs(sx, sy))



