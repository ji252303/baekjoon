import sys
input = sys.stdin.readline


def dfs(start,now,value,count):
    global ans
    if count == N:
        if a[now][start]:
            value += a[now][start]
            if ans > value:
                ans = value
        return

    if value > ans:
        return

    for i in range(N):
        if not visited[i] and a[now][i]:
            visited[i] = 1
            dfs(start, i ,value + a[now][i], count+1)
            visited[i] = 0

N = int(input())
a = [list(map(int, input().split()))for _ in range(N)]
ans = sys.maxsize
visited = [0] * N
for i in range(N):
    visited[i] = 1
    dfs(i, i, 0, 1)
    visited[i] = 0
print(ans)
