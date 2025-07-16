from typing import List, Tuple

def func(move: List[Tuple[int, int]]) -> None:
    l = [0]
    for v, t in move:
        for _ in range(t):
            k = l[-1]
            l.append(k+v)
    return l
        
n, m = map(int, input().split())
n_move = [tuple(map(int, input().split())) for _ in range(n)]
m_move = [tuple(map(int, input().split())) for _ in range(m)]

n_lst = func(n_move)
m_lst = func(m_move)

min_len = min(len(n_lst), len(m_lst))
dev_lst = [n_lst[i] - m_lst[i] for i in range(min_len)]

last_sign, ans = 0, 0
for x in dev_lst:
    if x == 0:
        continue

    curr_sign = 1 if x > 0 else -1
    if last_sign != 0 and curr_sign != last_sign:
        ans += 1
    last_sign = curr_sign

print(ans)