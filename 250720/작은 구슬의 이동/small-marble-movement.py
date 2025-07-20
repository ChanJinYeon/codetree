n, t = map(int, input().split())
r, c, d = input().split()
r, c = int(r)-1, int(c)-1

def in_range(r: int, c: int) -> bool:
    return 0 <= r < n and 0 <= c < n

dr, dc = [1, 0, 0, -1], [0, 1, -1, 0] # S, E, W, N
dirs = {"D": 0, "R": 1, "L": 2, "U": 3}
direction = dirs[d]

for i in range(t):
    nr, nc = r + dr[direction], c + dc[direction]

    if in_range(nr, nc):
        r, c = nr, nc
    else:
        direction = 3 - direction

print(r+1, c+1)