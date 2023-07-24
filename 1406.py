import sys

text_l = list(input())
text_r = []
n = int(input())

for i in range(n):
    command = sys.stdin.readline().split()

    if command[0] == "L" and text_l:
        text_r.append(text_l.pop())
    elif command[0] == "D" and text_r:
        text_l.append(text_r.pop())
    elif command[0] == "B" and text_l:
        text_l.pop()
    elif command[0] == "P":
        text_l.append(command[1])

print("".join(text_l+list(reversed(text_r))))

입력값:
abc
9
L
L
L
L
L
P x
L
B
P y

시작 값
stack_l = [a, b, c]
stack_r = []

L 입력
stack_l = [a, b]
stack_r = [c]

L 입력
stack_l = [a]
stack_r = [c, b]

L 입력
stack_l = []
stack_r = [c, b, a]

L 입력
stack_l의 값이 없어서 조건 불충족

L 입력
stack_l의 값이 없어서 조건 불충족

P x 입력
stack_l = [x]
stack_r = [c, b, a]

L 입력
stack_l = []
stack_r = [c, b, a, x]

B 입력
stack_l의 값이 없어서 조건 불충족

P y 입력
stack_l = [y]
stack_r = [c, b, a, x]

출력 
[y, x, a, b, c]
