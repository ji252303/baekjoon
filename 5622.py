a = input()
dial_list = ['ABC','DEF','GHI','JKL','MNO','PQRS','TUV','WXYZ']
time = 0

for i in range(len(a)):
    for j in dial_list:
        if a[i] in j:
            time += dial_list.index(j) + 3
print(time)
