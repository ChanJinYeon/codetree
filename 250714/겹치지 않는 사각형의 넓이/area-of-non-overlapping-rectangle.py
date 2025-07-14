N = 3
SIZE = 2001

rectangle = [map(int, input().split()) for _ in range(N)]
canvas = [[0] * SIZE for _ in range(SIZE)]

for i in range(len(rectangle)-1):
    x1, y1, x2, y2 = rectangle[i]
    for x in range(x1, x2):
        for y in range(y1, y2):
            canvas[x][y] = 1

x1, y1, x2, y2 = rectangle[-1]
for x in range(x1, x2):
    for y in range(y1, y2):
        canvas[x][y] = 0

print(sum(row.count(1) for row in canvas))
