N = int(input())
moves = [tuple(input().split()) for _ in range(N)]
drs, dcs = [-1, 0, 1, 0], [0, 1, 0, -1] # N, E, S, W
d_dict = {'N': 0, 'E': 1, 'S': 2, 'W': 3}

def solve():
    r = c = 0
    cnt = 0
    for d, t_str in moves:
        idx = d_dict[d]
        for _ in range(int(t_str)):
            r += drs[idx]
            c += dcs[idx]
            cnt += 1
            if r == 0 and c == 0:
                print(cnt)
                return
    print(-1)
    return

solve()