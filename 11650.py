import sys
input = sys.stdin.readline

n = int(input())

ar =[]

for i in range(n):
    [a,b] = map(int, input().split())
    ar.append([a,b])
    
s_ar= sorted(ar)
    
for i in range(n):
    print(s_ar[i][0],s_ar[i][1])
