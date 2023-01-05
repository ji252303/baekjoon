n, x = map(int,input().split())

alist = list(map(int, input().split()))

for i in range(n):
    if alist[i] < x:
        print(alist[i], end=" ")
