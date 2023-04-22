import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**7)

n = int(input())
card = sorted([*map(int, input().split())])
m = int(input())
find = [*map(int, input().split())]

count = {}

for i in card:
    if i in count:
        count[i] += 1
    else:
        count[i] = 1

def Search(arr, target, start, end):
    if start > end:
        return 0

    mid = (start + end) // 2
    if arr[mid] == target:
        return count.get(target)
    elif arr[mid] < target:
        return Search(arr, target, mid+1, end)
    else:
        return Search(arr, target, start, end-1)


for i in find:
    print(Search(card, i, 0, len(card)-1), end=" ")
