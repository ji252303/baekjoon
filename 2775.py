import sys
input = sys.stdin.readline

t = int(input())

for i in range(t):
    k = int(input())
    n = int(input())
    people = [i for i in range(1, n+1)]

    for j in range(k):
        new = []
        for x in range(n):
            new.append(sum(people[:x+1]))
        people = new.copy()
    print(people[-1])
