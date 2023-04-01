n= list(input())
n.sort(reverse=True)

num = ""

for i in n:
    num += i

if int(num) % 30 == 0:
    print(num)
else:
    print(-1)
