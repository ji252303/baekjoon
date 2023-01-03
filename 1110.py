n = int(input())
num = n
sum = 0
ct=0

while True:
    a = num // 10
    b = num % 10
    c= (a+b) % 10
    num  = (b * 10) + c

    ct = ct +1
    if(num == n):
        break

print(ct)
