import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**6)

n = int(input())

tree = [[]for _ in range(n+1)]
parent = [None for _ in range(n+1)]

def dfs(graph, vertex, visited):
    for i in graph[vertex]:
        if not visited[i]:
            visited[i] = vertex
            dfs(graph, i ,visited)

for _ in range(n-1):
    a, b = map(int, input().split())
    tree[a].append(b)
    tree[b].append(a)

dfs(tree, 1 ,parent)

for i in range(2, n+1):
    print(parent[i])
