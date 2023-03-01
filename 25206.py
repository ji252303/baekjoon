rate = ['A+', 'A0', 'B+', 'B0', 'C+', 'C0', 'D+', 'D0', 'F']
grade = [4.5, 4.0, 3.5, 3.0, 2.5, 2.0, 1.5, 1.0, 0]

total = 0
result = 0

for _ in range(20) :
    s, p, g = input().split()
    p = float(p)
    if g != 'P' :	
        total += p
        result += p * grade[rate.index(g)]
        
print('%.6f' % (result / total))
