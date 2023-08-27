import sys
sys.setrecursionlimit(100000)
input = sys.stdin.readline

def dfs(r, c):
    global cnt
    visit[r][c] = 1
    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]
        if 0 <= nr < m and 0 <= nc < n and visit[nr][nc] == 0:
            cnt += 1
            dfs(nr, nc)

m,n,k = map(int,input().split())

visit = [[0] * n for _ in range(m)]

for _ in range(k):
    sc, sr, ec, er = map(int,input().split())
    for i in range(sr,er):
        for j in range(sc,ec):
            visit[i][j] = 1

dr = [-1,0,1,0]
dc = [0,1,0,-1]
cnt = 1
area = 0
answer = []

for i in range(m):
    for j in range(n):
        if visit[i][j] == 0:
            area += 1
            dfs(i,j)
            answer.append(cnt)
            cnt = 1

answer.sort()
print(area)
print(' '.join(map(str, answer)))
