alist = [i for i in range(1,31)]

for i in range(28) :
    num = int(input())
    alist.remove(num)

print(min(alist))
print(max(alist))
