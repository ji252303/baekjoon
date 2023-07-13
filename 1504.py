import sys
from heapq import heappush, heappop
input = sys.stdin.readline
INF = 2147000000

def dijkstra(start,end):
    dis = [INF] * (n+1)
    dis[start] = 0
    q = [[0, start]]
    while q:
        k, u = heappop(q)
        if k > dis[u]:
            continue
        for i,j in g[u]:
            if dis[j] > dis[u] + i:
                dis[j] = dis[u] + i
                heappush(q, [dis[j], j])

    return dis[end]

n, e = map(int,input().split())
g = [[] for _ in range(n+1)]
for _ in range(e):
    u, v, w = map(int,input().split())
    g[u].append([w,v])
    g[v].append([w,u])

stop1, stop2 = map(int,input().split())

path1 = dijkstra(1, stop1) + dijkstra(stop1, stop2) + dijkstra(stop2, n)
path2 = dijkstra(1, stop2) + dijkstra(stop2, stop1) + dijkstra(stop1, n)

if path1 >= INF and path2 >= INF:
    print(-1)
else:
    print(min(path1,path2))

