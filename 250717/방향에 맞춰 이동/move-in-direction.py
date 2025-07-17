n = int(input())
move = [tuple(input().split()) for _ in range(n)]

r = c = 0
dr = [-1, 1, 0, 0]  # S, N, W, E
dc = [0, 0, -1, 1]
dic = {'S': 0, 'N': 1, 'W': 2, 'E': 3}

for d, v_str in move:
    v = int(v_str)
    r += dr[dic[d]] * v
    c += dc[dic[d]] * v

print(c, r)