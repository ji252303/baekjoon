import sys
sys.setrecursionlimit(100000)

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def dfs(x,y,h):
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if (0 <= nx < n) and (0 <= ny < n) and not sink_table[nx][ny] and water_board[nx][ny] > h:
            sink_table[nx][ny] = True
            dfs(nx,ny,h)


n = int(sys.stdin.readline())
water_board = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

ans = 1
for k in range(max(map(max, water_board))):
    sink_table = [[False] * n for _ in range(n)]
    count = 0
    for i in range(n):
        for j in range(n):
            if water_board[i][j] > k and not sink_table[i][j]:
                count += 1
                sink_table[i][j] = True
                dfs(i, j, k)

        ans = max(ans, count)

print(ans)
