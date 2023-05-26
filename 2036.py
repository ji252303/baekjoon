import sys
input = sys.stdin.readline

n = int(input())

posit = []
negat = []
one = []

for _ in range(n):
    num = int(input())
    if num > 1:
        posit.append(num)
    elif num <= 0:
        negat.append(num)
    else:
        one.append(num)

posit.sort(reverse=True)
negat.sort()

answer = 0

if len(posit) % 2 == 0:
    for i in range(0, len(posit), 2):
        answer += posit[i] * posit[i+1]
else:
    for i in range(0, len(posit)-1, 2):
        answer += posit[i] * posit[i+1]
    answer += posit[len(posit)-1]


if len(negat) % 2 == 0:
    for i in range(0, len(negat), 2):
        answer += negat[i] * negat[i+1]
else:
    for i in range(0, len(negat)-1, 2):
        answer += negat[i] * negat[i+1]
    answer += negat[len(negat)-1]

answer += sum(one)

print(answer)
