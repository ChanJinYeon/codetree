n = int(input())
grid = [list(input()) for _ in range(n)]
k = int(input()) - 1

def in_range(r: int, c: int) -> bool:
    return 0 <= r < n and 0 <= c < n

def slash(d: int) -> int:   # cf. drs, dcs
    direction = [1, 0, 3, 2]
    return direction[d]

def back_slash(d: int) -> int:  # cf. drs, dcs
    return 3 - d


r = c = 0
cnt = 0
d = 0
drs, dcs = [0, -1, 0, 1], [1, 0, -1, 0] # E, N, W, S
start_dir = k // 4
start_num = k % 4

if start_dir == 0:
    r = 0
    c = start_num
    d = 3
elif start_dir == 1:
    r = start_num
    c = n - 1
    d = 2
elif start_dir == 2:
    r = n - 1
    c = n - 1 - start_num
    d = 1
else:
    r = n - 1 - start_num
    c = 0
    d = 0

while True:
    cnt += 1
    if grid[r][c] == '/':
        d = slash(d)
        nr, nc = r + drs[d], c + dcs[d]
        if in_range(nr, nc):
            r, c = nr, nc
        else:
            break
    else:
        d = back_slash(d)
        nr, nc = r + drs[d], c + dcs[d]
        if in_range(nr, nc):
            r, c = nr, nc
        else:
            break

print(cnt)