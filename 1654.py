import sys

input = sys.stdin.readline

k, n = map(int, input().split())
ar = []

for i in range(k):
    ar.append(int(input()))
    
start = 1
end = max(ar)

while (start <= end):
    mid = (start + end) // 2
    count = 0
    for i in range(k):
        count += ar[i] // mid
    if count >= n:
        start = mid+1
    else:
        end = mid -1
        
print(end)
