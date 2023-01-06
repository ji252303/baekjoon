num = set(range(1,10001))
notself = set()

for i in range(1,10001):
    for j in str(i):
        i += int(j)
    notself.add(i)

self = sorted(num - notself)
for i in self:
    print(i)
