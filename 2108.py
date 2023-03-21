import sys
input = sys.stdin.readline

n = int(input())
a = []

for i in range(n):
    a.append(int(input()))

a.sort()

print(round(sum(a)/len(a)))
print(a[len(a)//2])

dic = dict()
for i in a:
    if i in dic:
        dic[i] +=1
    else:
        dic[i] = 1

mx = max(dic.values())
mx_dic = []

for i in dic:
    if mx==dic[i]:
        mx_dic.append(i)

if len(mx_dic)>1:
    print(mx_dic[1])
else:
    print(mx_dic[0])

print(max(a)-min(a))
