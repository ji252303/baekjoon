n = int(input())
people = list(map(int, input().split()))

people.sort()
sum = 0

for i in range(n):
    for j in range(i+1):
      sum += people[j]

print(sum)
