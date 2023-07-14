from collections import deque

n, k = map(int, input().split())
q = deque()
q.append(n)
dist = [-1 for _ in range(100001)]
dist[n] = 0

while q:
    target = q.popleft()
    if target == k:
        print(dist[target])
        break
    if 0 <= target - 1 < 100001 and dist[target-1] == -1:
        dist[target - 1] = dist[target] + 1
        q.append(target - 1)
    if 0 < target*2 < 100001 and dist[target*2] == -1:
        dist[target * 2] = dist[target]
        q.appendleft(target*2)
    if 0 <= target + 1 < 100001 and dist[target+1] == -1:
        dist[target + 1] = dist[target] + 1
        q.append(target+1)
