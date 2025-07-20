N = int(input())
moves = [tuple(input().split()) for _ in range(N)]

r = c = d = 0
drs, dcs = [-1, 0, 1, 0], [0, 1, 0, -1] # N, E, S, W
d_dict = {'N': 0, 'E': 1, 'S': 2, 'W': 3}

ans = -1
cnt = 0
f = False
for d, t_str in moves:
    t = int(t_str)
    for _ in range(t):
        nr, nc = r + drs[d_dict[d]], c + dcs[d_dict[d]]
        r, c = nr, nc
        cnt += 1
        if r == 0 and c == 0:
            f = True
            break   
    if f:
        ans = cnt
        break

print(ans)