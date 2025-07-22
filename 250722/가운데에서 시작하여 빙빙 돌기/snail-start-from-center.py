n = int(input())
grid = [[0] * n for _ in range(n)]

def in_range(r: int, c: int) -> bool:
    return 0 <= r < n and 0 <= c < n

t = n * n
r = c = n - 1
cnt = t
d = 0
grid[r][c] = cnt
drs, dcs = [0, -1, 0, 1], [-1, 0, 1, 0] # W, N, E, S

for _ in range(t-1):
    cnt -= 1
    nr, nc = r + drs[d], c + dcs[d]

    if not in_range(nr, nc) or grid[nr][nc] != 0:
        d = (d + 1) % 4
        nr, nc = r + drs[d], c + dcs[d]
    r, c = nr, nc
    grid[r][c] = cnt

for row in grid:
    print(*row, sep=' ')