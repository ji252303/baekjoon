n = int(input())
line = 1
while n > line:
    n -= line
    line += 1

if line%2==0:
    u = n
    p = line-n+1
else:
    u = line-n+1
    p= n

print(u,'/',p, sep='')
