docu = input().strip()
sear = input().strip()

count = 0
index = 0

for i in range(len(docu)):
    if index > i:
        continue
    if sear == docu[i: i+len(sear)]:
        count += 1
        index = i + len(sear)

print(count)
