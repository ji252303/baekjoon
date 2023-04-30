n = list(input())

zero = n.count('0')//2
one = n.count('1')//2

for _ in range(zero):
    n = n[::-1]
    n.remove('0')
    n = n[::-1]
for _ in range(one):
    n.remove('1')

print(''.join(n))
