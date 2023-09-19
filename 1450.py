import sys

n,c = map(int,sys.stdin.readline().split())
weight = list(map(int,sys.stdin.readline().split()))
a = weight[:n//2]
b = weight[n //2:]
a_sum = []
b_sum = []

def brute(w_arr,sum_arr,l,w):
    if l >= len(w_arr):
        sum_arr.append(w)
        return
    brute(w_arr,sum_arr,l+1,w)
    brute(w_arr,sum_arr,l+1,w+w_arr[l])

def binarysearch(arr,target,start,end):
    while start < end:
        mid = (start + end) //2
        if arr[mid] <= target:
            start = mid + 1
        else:
            end = mid
    return end


brute(a,a_sum,0,0)
brute(b,b_sum,0,0)
b_sum.sort()

count = 0

for i in a_sum:
    if c - i < 0:
        continue
    count += binarysearch(b_sum,c-i,0,len(b_sum))
print(count)
