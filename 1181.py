n = int(input())
lst= []

for i in range(n):
    lst.append(input())

set_list = set(lst)
lst = list(set_list)
lst.sort()
lst.sort(key = len)

for i in lst:
    print(i)
