import sys
input = sys.stdin.readline

n, m = map(int,input().split())
data = list(map(int, input().split()))
data.sort()
visited = [False] * n
out = []

def dfs():
    if len(out) == m:
        print(' '.join(map(str, out)))
        return

    for i in range(n):
        if not visited[i]:
            out.append(data[i])
            visited[i]= True
            dfs()
            visited[i] = False
            out.pop()
            
dfs()
