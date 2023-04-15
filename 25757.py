import sys
input = sys.stdin.readline

n, k = input().split()
people = set()
for _ in range(int(n)):
    people.add(input().rstrip())
    
a = len(people)

if k == 'Y':
    print(a)
elif k == 'F':
    print(a//2)
else:
    print(a//3)
