from collections import deque
import sys

input = sys.stdin.readline

n, m = map(int, input().split())
graph = [list(map(int, input().rstrip())) for _ in range(n)]

move = [[[0, 0] for _ in range(m)] for _ in range(n)]

dx = [0,0,1,-1]
dy = [1,-1,0,0]


def bfs(x, y):
    queue = deque([(x, y, 0)])
    move[y][x][0] = 1

    while queue:
        x,y,bre_count = queue.popleft()

        if(x,y) == (m-1, n-1):
            return move[y][x][bre_count]

        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            if 0 <= nx < m and 0 <= ny < n:
                if graph[ny][nx] == 1 and bre_count == 0:
                    move[ny][nx][1] = move[y][x][0] + 1
                    queue.append([nx, ny, 1])

                if graph[ny][nx] == 0 and move[ny][nx][bre_count] == 0:
                    move[ny][nx][bre_count] == move[y][x][bre_count] + 1
                    queue.append([nx, ny, bre_count])
    return -1

print(bfs(0, 0))
위는 시간초과 코드....
  
import sys
from collections import deque

input = sys.stdin.readline
N, M = map(int, input().split())
board = [list(map(int, input().rstrip())) for _ in range(N)]
visited = [[[0] * 2 for _ in range(M)] for _ in range(N)]
dir = [[-1, 0], [1, 0], [0, -1], [0, 1]]
ans = 0


def bfs():
    q = deque([(0, 0, 0)])
    visited[0][0][0] = 1

    while q:
        r, c, wall = q.popleft()
        if r == N - 1 and c == M - 1:
            return visited[r][c][wall]

        for i in range(4):
            nr = r + dir[i][0]
            nc = c + dir[i][1]
            if 0 <= nr < N and 0 <= nc < M and visited[nr][nc][wall] == 0:
                # 벽이 아니라면 이동하고, 이전경로 + 1 visited 배열에 저장
                if board[nr][nc] == 0:
                    q.append((nr, nc, wall))
                    visited[nr][nc][wall] = visited[r][c][wall] + 1

                # 벽 1번도 안 부쉈고, 다음 이동할 곳이 벽이라면
                if wall == 0 and board[nr][nc] == 1:
                    # 벽을 부순 상태를 1로 표현
                    q.append((nr, nc, 1))
                    visited[nr][nc][1] = visited[r][c][wall] + 1

    return -1


print(bfs())


