import sys
from collections import deque
input = sys.stdin.readline

def bfs():
    queue = deque([1])
    visited[1] = True
    while queue:
        now = queue.popleft()
        for m in range(1,7):
            check = now + m
            if 0 < check <= 100 and not visited[check]:
                if check in ladder.keys():
                    check = ladder[check]
                if check in snake.keys():
                    check = snake[check]

                if not visited[check]:
                    queue.append(check)
                    visited[check] = True
                    count[check] = count[now] + 1

if __name__ == '__main__':
    n, m = map(int, input().split())
    count = [0] * 101
    visited = [False] * 101

    snake = dict()
    ladder = dict()
    for _ in range(n):
        i,j = map(int,input().split())
        ladder[i] = j
    for _ in range(m):
        i,j = map(int,input().split())
        snake[i] = j

    bfs()
    print(count[100])
