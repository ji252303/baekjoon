import sys
input = sys.stdin.readline

n = int(input())
top = list(map(int,input().split()))
result = [0] * n
stack = []

for i in range(len(top)):
    t = top[i]
    while stack and top[stack[-1]] < t:
        stack.pop()
    if stack:
        result[i] = stack[-1] + 1
    stack.append(i)

print(' '.join(list(map(str,result))))
