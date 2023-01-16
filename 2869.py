a,b,v = map(int,input().split())

day = (v-b) / (a-b)
if day == int(day):
    print(int(day))
else:
    print(int(day)+1)
