import sys
import heapq
n, d = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(d+1)]

for i in range(d):
    graph[i].append((i+1, 1))

for i in range(n):
    start, end, length = map(int, sys.stdin.readline().split())
    if end > d:
        continue
    graph[start].append((end, length))

INF = 987654321
distance = [INF]*(d+1)
distance[0] = 0

q = []
heapq.heappush(q, (0, 0))

while q:
    a, now = heapq.heappop(q)
    if distance[now] < a:
        continue

    for x in graph[now]:
        cost = a + x[1]

        if distance[x[0]] > cost:
            distance[x[0]] = cost
            heapq.heappush(q, (cost, x[0]))

print(distance[d])
