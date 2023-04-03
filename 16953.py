a, b = map(int, input().split())

count = 1
while(b!=a):
    count += 1
    temp = b
    if b%10 == 1:
        b//=10
    elif b%2 == 0:
        b//=2

    if temp == b:
        print(-1)
        break

else:
    print(count)
