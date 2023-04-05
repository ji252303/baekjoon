n = int(input())
point = sorted(map(int, input().split()))
abc = []
a_min = []
b_min = []

for i in range(n-1):
    abc.append(point[i + 1] - point[i])

for j in abc:
    if j % 2 == 0:
        a_min.append(j)
    elif (j+(j+1)) % 2 == 0:
        a_min.append(j+(j+1))
    else:
        b_min.append(j)

if not a_min and len(b_min) > 1:
    a_min.append(b_min[0]+b_min[1])

if not a_min:
    print(-1, min(b_min))
elif not b_min:
    print(min(a_min), -1)
else:
    print(min(a_min), min(b_min))
