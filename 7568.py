n = int(input())

data = []
rank = []

for i in range(n):
    a, b = map(int,input().split())
    data.append((a,b))

for i in range(n):
    cnt = 0
    for j in range(n):
        if data[i][0] < data[j][0] and data[i][1] < data[j][1]:
            cnt +=1
    rank.append(cnt + 1)

for k in rank:
    print(k,end=' ')
