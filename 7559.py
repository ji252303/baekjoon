import sys
import collections
input = sys.stdin.readline

dx = [-1,1,0,0,0,0]
dy = [0,0,-1,1,0,0]
dz = [0,0,0,0,-1,1]
m, n, h = map(int, input().split())
graph = [[list(map(int,input().split())) for _ in range(n)] for _ in range(h)]
visited = [[[False]*m for _ in range(n)] for _ in range(h)]
queue = collections.deque()
answer = 0


def bfs():
    while queue:
        x, y, z = queue.popleft()
        for a in range(6):
            nx = x + dx[a]
            ny = y + dy[a]
            nz = z + dz[a]

            if nx < 0 or nx >= h or ny < 0 or ny >= n or nz < 0 or nz >= m:
                continue

            if graph[nx][ny][nz] == 0 and visited[nx][ny][nz] == False:
                queue.append((nx,ny,nz))
                graph[nx][ny][nz] = graph[x][y][z] + 1
                visited[nx][ny][nz] = True


for i in range(h):
    for j in range(n):
        for k in range(m):
            if graph[i][j][k] == 1 and visited[i][j][k] == 0:
                queue.append((i, j, k))
                visited[i][j][k] = True

bfs()

for a in graph:
    for b in a:
        for c in b:
            if c == 0:
                print(-1)
                exit(0)
        answer = max(answer, max(b))

print(answer-1)
