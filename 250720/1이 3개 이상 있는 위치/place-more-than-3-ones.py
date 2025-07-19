def in_range(r: int, c: int):
    return 0 <= r < n and 0 <= c < n

n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

drs, dcs = [1, 0, -1, 0], [0, 1, 0, -1]

ans = 0
for i in range(n):
    for j in range(n):
        r, c = i, j
        cnt = 0
        for dr, dc in zip(drs, dcs):
            nr, nc = r + dr, c + dc
            if in_range(nr, nc) and grid[nr][nc] == 1:
                cnt += 1
        if cnt >= 3:
            ans += 1

print(ans)