import sys
import copy

input = sys.stdin.readline

def back(v):
    if len(v) == n-1:
        arr.append(copy.deepcopy(v))
        return

    v.append(' ') #34
    back(v)
    v.pop()

    v.append('+') #44
    back(v)
    v.pop()

    v.append('-') #45
    back(v)
    v.pop()


t = int(input())

for _ in range(t):
    n = int(input())
    arr = []
    back([])

    for i in arr:
        temp = ''
        for j in range(1,n):
            temp += str(j) + str(i[j-1])
        temp += str(n)

        if eval(temp.replace(' ','')) == 0:
            print(temp)
    print()
