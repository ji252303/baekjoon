import heapq

def dijkstra(s):
    d = [float('inf')] * (n+1)
    d[s] = 0
    q = []
    heapq.heappush(q, (0,s))
    while q:
        dist, now = heapq.heappop(q)
        if d[now] >= dist:
            for v, val in city[now]:
                if dist + val < d[v]:
                    d[v] = dist + val
                    heapq.heappush(q, (dist+val,v))
    return d


n,m,x = map(int, input().split())
city = [[] for _ in range(n+1)]
for _ in range(m):
    a,b,t = map(int,input().split())
    city[a].append([b,t])

answer = dijkstra(x)
answer[0] = 0

for i in range(1, n+1):
    if i != x:
        res = dijkstra(i)
        answer[i] += res[x]

print(max(answer))
