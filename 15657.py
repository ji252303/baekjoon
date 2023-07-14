import sys
input = sys.stdin.readline

n, m = map(int,input().split())
data = list(map(int, input().split()))
data.sort()
out =[]

def dfs(s):
    if len(out) == m:
        print(' '.join(map(str, out)))
        return

    for i in range(s, n):
        out.append(data[i])
        dfs(i)
        out.pop()

dfs(0)
