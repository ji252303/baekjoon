import sys
input = sys.stdin.readline

point = int(input())
n= int(input())
if n == 0:
     broken_button = []
else:
     broken_button = list(map(int, input().split()))

count = abs(100-point) #+와 -만 사용하는 경우

for num in range(1000001):
    num = str(num)
    for j in range(len(num)):
        if int(num[j]) in broken_button:
            break
    else:
        count = min(count, len(num) + abs(int(num)-point))

print(count)
