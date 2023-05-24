import sys
input = sys.stdin.readline

n, k = map(int, input().split())
num = input().rstrip()

stack = []

for i in num:
    while stack and stack[-1] < i and k > 0:
        stack.pop()
        k -= 1
    stack.append(i)

if k > 0:
    print(''.join(stack[:-k]))
else:
    print(''.join(stack))
