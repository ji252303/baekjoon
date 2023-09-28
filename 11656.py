import sys
input = sys.stdin.readline

n = input().rstrip()
answer = []

for i in range(len(n)):
    answer.append(n[i:])

answer.sort()

for i in answer:
    print(i)
