import sys
import heapq
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

n, m = map(int, input().split())
k = int(input())

inf = int(1e9)

graph = [[] * (n+1) for _ in range(n+1)]
distance = [inf] * (n+1)

for _ in range(m):
    a,b,c = map(int, input().split())
    graph[a].append((b,c))

def extra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0

    while q:
        # 가장 최단 거리가 짧은 노드에 대한 정보 꺼내기
        dist, now = heapq.heappop(q)
        # 현재 노드가 이미 처리된 적이 있는 노드라면 무시
        if distance[now] < dist:
            continue
        # 현재 노드와 연결된 다른 인접한 노드들을 확인
        for i in graph[now]:
            cost = dist + i[1]
        # 현재 노드를 거쳐서, 다른 노드로 이동하는 거리가 더 짧은 경우
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

extra(k)

for i in range(1, n+1):
    if distance[i] == inf:
        print("INF")
    else:
        print(distance[i])

