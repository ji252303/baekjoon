from collections import deque
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)

n , m , r = map(int,input().split())
graph = [[0] * (n+1) for _ in range(n+1)]
visited1 = [0] * (n+1)
visited2 = [0] * (n+1)


for _ in range(m):
    a,b = map(int, input().split())
    graph[a][b] = graph[b][a] = 1


def dfs(start):
    visited2[start] = 1
    print(start, end = " ")
    for i in range(1, n+1):
        if visited2[i] == 0 and graph[start][i] == 1:
            dfs(i)

def bfs(start):
    q = deque()
    q.append(start)
    visited1[start] = 1
    while q:
        start = q.popleft()
        print(start, end = ' ')
        for i in range(1, n+1):
            if visited1[i] == 0 and graph[start][i] == 1:
                q.append(i)
                visited1[i] = 1



dfs(r)
print()
bfs(r)
