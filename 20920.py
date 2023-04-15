import sys
input = sys.stdin.readline

n, m = map(int, input().rstrip().split())
list = {}

for _ in range(n):
    word = input().rstrip()

    if len(word) < m:
        continue
    else:
        if word in list:
            list[word] += 1
        else:
            list[word] = 1


list = sorted(list.items(), key = lambda x : (-x[1], -len(x[0]), x[0]))

for i in list:
    print(i[0])
