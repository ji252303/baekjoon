import sys
from collections import deque
input = sys.stdin.readline

max = 100001
n , m = map(int, input().split())
visited = [0] * max

def bfs():
    q = deque()
    q.append(n)

    while q:
        a = q.popleft()
        if a == m:
            print(visited[a])
            break
        for i in (a-1, a+1, a*2):
            if 0 <= i < max and visited[i] == 0:
                visited[i] = visited[a] + 1
                q.append(i)

bfs()
