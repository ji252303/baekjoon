import sys
input = sys.stdin.readline

S = input().rstrip()
explosion_string = input().rstrip()

stack = []
ex_len = len(explosion_string)

for i in range(len(S)):
    stack.append(S[i])
    if ''.join(stack[-ex_len:]) == explosion_string:
        for _ in range(ex_len):
            stack.pop()

# 결과 출력
if stack:
    print(''.join(stack))
else:
    print('FRULA')
