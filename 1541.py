a = input().split('-')
sum = 0

for i in a[0].split('+'):
    sum += int(i)

for i in a[1:]:
    for j in i.split("+"):
        sum-= int(j)

print(sum)
