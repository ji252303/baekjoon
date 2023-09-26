import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int,input().split())
graph = [[] for _ in range(n+1)]
degree = [0] * (n+1)

for _ in range(m):
    a, b = map(int,input().split())
    graph[a].append(b)
    degree[b] += 1

q = deque()

for i in range(1, n+1):
    if degree[i] == 0:
        q.append(i)

answer = []

while q:
    c = q.popleft()
    answer.append(c)

    for j in graph[c]:
        degree[j] -= 1
        if degree[j] == 0:
            q.append(j)

print(*answer, sep =" ")
