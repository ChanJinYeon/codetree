N = 2
SIZE = 2001
OFFSET = 1000

rec = [tuple(map(int, input().split())) for _ in range(N)]
canvas = [[0] * SIZE for _ in range(SIZE)]

for i in range(0, N):
    x1, y1, x2, y2 = rec[i]
    for x in range(x1+OFFSET, x2+OFFSET):
        for y in range(y1+OFFSET, y2+OFFSET):
            canvas[x][y] = 1 if i == 0 else 0

min_x = min_y = SIZE
max_x = max_y = -1

for x in range(SIZE):
    for y in range(SIZE):
        if canvas[x][y] == 1:
            min_x = min(min_x, x)
            min_y = min(min_y, y)
            max_x = max(max_x, x)
            max_y = max(max_y, y)

if max_x < min_x or max_y < min_y:
    print(0)
else:
    w = max_x - min_x + 1
    h = max_y - min_y + 1
    print(w * h)