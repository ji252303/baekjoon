import sys
input = sys.stdin.readline
n = int(input())
num = list(map(int, input().split()))
ar = sorted(set(num))

dic = {}
for i in range(len(ar)):
    dic[ar[i]] = i

for i in num:
    print(dic[i],end=' ')
