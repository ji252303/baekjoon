n = int(input())

stack = []

for i in range(n):
    a = input()
    sum=0
    for j in a:
        if j =='(':
            sum+=1
        elif j == ')':
            sum-=1
        if sum < 0:
            print("NO")
            break

    if sum > 0:
        print("NO")
    elif sum == 0:
        print("YES")
