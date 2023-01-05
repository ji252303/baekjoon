alist = []
for i in range(10):
    n = int(input())
    alist.append(n % 42)

s = set(alist)
print(len(s))
