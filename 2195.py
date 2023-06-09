import sys

input = sys.stdin.readline

s = input().rstrip()
p = input().rstrip()

answer = 0

id = 0

while id < len(p):
    copy = ''

    if s.find(p[id:]) != -1:
        answer += 1
        break

    for i in range(id, len(p)):
        copy += p[i]
        if s.find(copy) == -1:
            answer += 1
            id = i
            break

print(answer)
