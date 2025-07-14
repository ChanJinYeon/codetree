N = 2
SIZE = 2001
OFFSET = 1000

rec = [map(int, input().split()) for _ in range(N)]
canvas = [[0] * SIZE for _ in range(SIZE)]

min_x = 1000
max_x = -1000

max_y = -1000