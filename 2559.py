import sys
input = sys.stdin.readline

n, k = map(int,input().split())
temp = list(map(int,input().split()))

sum_list = sum(temp[:k])
result = [sum_list]

for i in range(0,len(temp)-k):
    sum_list = sum_list - temp[i] + temp[i+k]
    result.append(sum_list)

print(max(result))
