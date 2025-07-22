n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

cnt = 0
for r in range(n):
    for c in range(0, n-2):
        cnt = max(cnt, grid[r][c] + grid[r][c+1] + grid[r][c+2])
print(cnt)
