import sys
input = sys.stdin.readline

n = int(input())
r = int(input())
c = [[] for i in range(n+1)]
q = []
visited = [0] * (n+1)

for i in range(r):
    c1, c2 = map(int, input().split())
    c[c1].append(c2)
    c[c2].append(c1)


q.append(1)

while q:
    temp = q.pop(0)
    visited[temp] = 1
    for i in c[temp]:
        if visited[r] != 1:
            visited[i] = 1
            q.append(i)

print(visited[2:].count(1))
