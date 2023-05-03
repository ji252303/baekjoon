import sys
import collections

input = sys.stdin.readline
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
m, n = map(int, input().split())
graph = [list(map(int,input().split())) for _ in range(n)]
queue = collections.deque()

for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:
            queue.append((i, j))


while queue:
    i, j = queue.popleft()
    for k in range(4):
        di = i + dx[k]
        dj = j + dy[k]
        if 0 <= di < n and 0 <= dj < m and graph[di][dj] == 0:
            graph[di][dj] = graph[i][j] + 1
            queue.append((di, dj))


answer = max(map(max, graph)) - 1

for row in graph:
    if 0 in row:
        answer = -1

print(answer)
