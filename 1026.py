n = int(input())

alist = list(map(int,input().split()))
blist = list(map(int,input().split()))

sum = 0

for i in range(n):
    sum += min(alist) * max(blist)
    alist.pop(alist.index(min(alist)))
    blist.pop(blist.index(max(blist)))

print(sum)
