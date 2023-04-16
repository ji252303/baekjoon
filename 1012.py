import sys
input = sys.stdin.readline

test = int(input())

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs(x,y):
    queue = [(x,y)]
    visited[x][y] = 0

    while queue:
        x,y = queue.pop(0)

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= m or ny < 0 or ny >= n:
                continue

            if visited[nx][ny] == 1:
                queue.append((nx,ny))
                visited[nx][ny] = 0 #방문처리

for i in range(test):
    m, n, k = map(int, input().split())
    visited = [[0]*(n) for _ in range(m)]
    count = 0

    for j in range(k):
        x,y = map(int, input().split()) #지렁이 위치
        visited[x][y] = 1

    for a in range(m):
        for b in range(n):
            if visited[a][b] == 1:
                bfs(a, b)
                count += 1

    print(count)

