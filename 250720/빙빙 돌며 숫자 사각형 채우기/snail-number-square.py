n, m = map(int, input().split())
arr = [[0] * m for _ in range(n)]
t = n * m

r = c = d = 0
dr, dc = [0, 1, 0, -1], [1, 0, -1, 0]   # E, S, W, N

arr[r][c] = 1
cnt = 2

for i in range(2, t + 1):
    nr, nc = r + dr[d], c + dc[d]

    if not (0 <= nr < n and 0 <= nc < m) or arr[nr][nc] != 0:
        d = (d + 1) % 4

    r, c = r + dr[d], c + dc[d]
    arr[r][c] = i

for row in arr:
    print(*row, sep=' ')
