a = int(input())

han = 0

for i in range(1, a+1):
    alist = list(map(int, str(i)))
    if i <100:
        han += 1
    elif alist[0]-alist[1] == alist[1] - alist[2]:
        han += 1
print(han)
