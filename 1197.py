from heapq import heappush, heappop
import sys
input = sys.stdin.readline


def prim(start, weight):
    visit = [0] * (V+1)
    q = [[weight, start]]
    answer = 0
    count = 0
    while count < V:
        k,v = heappop(q)
        if visit[v]:
            continue
        visit[v] = 1
        answer += k
        count += 1
        for u,w in g[v]:
            heappush(q,[w,u])
    return answer



V, E = map(int,input().split())
g = [[] for _ in range(V+1)]
for _ in range(E):
    u,v,w = map(int,input().split())
    g[u].append([v,w])
    g[v].append([u,w])

print(prim(1,0))
