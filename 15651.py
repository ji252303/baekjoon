import sys
input = sys.stdin.readline

def dfs(count):
    if count == m:
        print(' '.join(map(str, ar)))
        return
    for i in range(1, n+1):
        ar[count] = i
        dfs(count+1)
    
n, m = map(int,input().split())
ar = [0 for _ in range(m)]
dfs(0)
