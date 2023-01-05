n = int(input())
alist = list(map(int, input().split()))

blist = []
for i in range(n):
    blist.append(alist[i]/max(alist)*100)

avg= sum(blist)/n
print(avg)
