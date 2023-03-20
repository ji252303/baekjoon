import sys
from collections import deque
n , k = map(int,sys.stdin.readline().split())
q = deque()
result = []

for i in range(1, n+1):
    q.append(i)

while q:
    for i in range(k-1):
        q.append(q.popleft())
    result.append(q.popleft())

print("<", end='')
print(', '.join(map(str,result)), end='')
print(">")
