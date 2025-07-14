n = int(input())
rec = [map(int, input().split()) for _ in range(n)]

SIZE = 201

canvas = [[0] * SIZE for _ in range(SIZE)]

for x1, y1, x2, y2 in rec:
    for y in range(y1, y2):
        for x in range(x1, x2):
            canvas[x][y] = 1
        
ans = sum(row.count(1) for row in canvas)
print(ans)