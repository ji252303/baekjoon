n,m = map(int,input().split())
pack = []
piece = []

for _ in range(m):
    a, b = map(int,input().split())
    pack.append(a)
    piece.append(b)

min_pack = min(pack)

result = 0

while n > 0:

    if n >= 6:
        min_piece = min(piece)*6
        n -= 6
    else:
        min_piece = min(piece)*n
        n -= n

    if min_piece < min_pack:
        result += min_piece
    else:
        result += min_pack

print(result)
