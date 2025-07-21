n, m = map(int, input().split())
grid = [[0] * m for _ in range(n)]
t = n * m

def in_range(r: int, c: int) -> bool:
    return 0 <= r < n and 0 <= c < m

r = c = 0
d = 0
cnt = 1
drs, dcs = [1, 0, -1, 0], [0, 1, 0, -1] # S, E, N, W

grid[0][0] = 1
for _ in range(t-1):
    cnt += 1
    nr, nc = r + drs[d], c + dcs[d]
    if not in_range(nr, nc) or grid[nr][nc] != 0:
        d = (d + 1) % 4

    r, c = r + drs[d], c + dcs[d]
    grid[r][c] = cnt

for row in grid:
    print(*row, sep=' ')
