import sys
input = sys.stdin.readline

n = int(input())
commands = [tuple(input().split()) for _ in range(n)]

SIZE = 200_001
idx = 100_000

lst = [[0, 0, 0] for _ in range(SIZE)]  # [0] = state, [1] [2] = w/b cnt

min_idx = idx
max_idx = idx

for a_str, b in commands:
    a = int(a_str)

    if b == 'L':
        new_idx = idx - a + 1
        s, e = new_idx, idx
    else:
        new_idx = idx + a - 1
        s, e = idx, new_idx

    for i in range(s, e + 1):
        state, w_cnt, b_cnt = lst[i]
        if state != 2:
            if b == 'L':
                w_cnt += 1
            else:
                b_cnt += 1

        if w_cnt >= 2 and b_cnt >= 2:
            state = 2
        else:
            state = -1 if b == 'L' else 1
    
        lst[i] = [state, w_cnt, b_cnt]
    
    idx = new_idx
    min_idx = min(min_idx, s)
    max_idx = max(max_idx, e)

w = b = g = 0

for i in range(min_idx, max_idx + 1):
    state = lst[i][0]

    if state == 2:
        g += 1
    elif state == -1:
        w += 1
    elif state == 1:
        b += 1
    
print(w, b, g)
