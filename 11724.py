import sys
input = sys.stdin.readline
sys.setrecursionlimit(10000)

n, m = map(int, input().split())
arr = [[] for _ in range(n+1)]
visited = [False] * (n+1)
count = 0


def dfs(v):
    visited[v] = True
    for i in arr[v]:
        if not visited[i]:
            dfs(i)
            
for _ in range(m):
    u, v = map(int, input().split())
    arr[u].append(v)
    arr[v].append(u)
    
for j in range(1, n+1):
    if not visited[j]:
        dfs(j)
        count +=1
        
print(count)
