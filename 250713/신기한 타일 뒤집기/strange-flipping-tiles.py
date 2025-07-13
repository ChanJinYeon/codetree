n = int(input())
commands = [tuple(input().split()) for _ in range(n)]

SIZE = 200_001
idx = 100_000
min_idx = idx
max_idx = idx

lst = [0 for _ in range(SIZE)]

for a_str, b in commands:
    a = int(a_str)

    if b == 'L':
        new_idx = idx - a + 1
        s, e = new_idx, idx
    else:
        new_idx = idx + a - 1
        s, e = idx, new_idx

    for i in range(s, e + 1):
        if b == 'L':
            lst[i] = -1
        else:
            lst[i] = 1
    
    idx = new_idx
    min_idx = min(min_idx, s)
    max_idx = max(max_idx, e)

w = b = 0
for i in range(min_idx, max_idx + 1):
    if lst[i] == -1:
        w += 1
    elif lst[i] == 1:
        b += 1

print(w, b)