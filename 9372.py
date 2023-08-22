import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def dfs(node, count):
    visited[node] = 1

    for i in graph[node]:
        if visited[i] == 0:
            count = dfs(i, count+1)
    return count


t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    graph = [[] for _ in range(n+1)]
    visited = [0]*(n+1)

    for _ in range(m):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)

    print(dfs(1,0))
