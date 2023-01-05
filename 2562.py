alist = []
for i in range(9) :
    alist.append(int(input())) 

print(max(alist))
print(alist.index(max(alist))+1)
