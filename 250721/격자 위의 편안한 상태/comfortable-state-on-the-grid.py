def solve():
    n, m = map(int, input().split())
    points = [tuple(map(int, input().split())) for _ in range(m)]
    grid = [[0]*(n+1) for _ in range(n+1)]
    
    drs, dcs = [-1, 0, 1, 0], [0, 1, 0, -1] # N, E, S, W

    for r, c in points:
        cnt = 0
        grid[r][c] = 1
        for dr, dc in zip(drs, dcs):
            nr, nc = r + dr, c + dc
            if 1 <= nr < n+1 and 1 <= nc < n+1 and grid[nr][nc] == 1:
                cnt += 1
        print(1 if cnt == 3 else 0)
    return

solve()