import math

K = input()

prev = ''
A, B = 0, 0
op = ''
for i in range(len(K)):
    if (prev.isdigit() and not K[i].isdigit()):
        op = K[i]
        A = int(K[:i], 8)
        B = int(K[i + 1:], 8)
    prev = K[i]

if (op == '/' and B == 0):
    print('invalid')
    exit(0)

rst = oct(math.floor((eval(str(A) + op + str(B)))))
if rst[0] == '-':
    print('-' + rst[3:])
else:
    print(rst[2:])
