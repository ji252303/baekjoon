point = []

for i in range(int(input())):
    x, y = map(int, input().split())
    point.append((x,y))

point.sort(key= lambda x : (x[1], x[0]))

for j in point:
    print(j[0], j[1])
