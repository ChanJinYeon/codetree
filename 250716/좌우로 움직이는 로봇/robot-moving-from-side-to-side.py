from typing import List, Tuple

def func(move: List[Tuple[int, int]]) -> List[int]:
    lst = [0]
    for m_str, d in move:
        m = int(m_str)
        step = 1 if d == 'R' else -1
        for _ in range(m):
            lst.append(lst[-1] + step)
    return lst

n, m = map(int, input().split())
n_move = [tuple(input().split()) for _ in range(n)]
m_move = [tuple(input().split()) for _ in range(m)]

n_lst = func(n_move)
m_lst = func(m_move)
len_n_lst = len(n_lst)
len_m_lst = len(m_lst)
max_len = max(len_n_lst, len_m_lst)
min_len = min(len_n_lst, len_m_lst)

for _ in range(min_len, max_len):
    if len_n_lst > len_m_lst:
        m_lst.append(m_lst[-1])
    else:
        n_lst.append(n_lst[-1])

dev_lst = [n_lst[i] - m_lst[i] for i in range(max_len)]

ans = 0
last_sign = 0
    
for x in dev_lst:
    if x == 0:
        continue
    
    curr_sign = 1 if x > 0 else -1

    if last_sign != 0 and curr_sign != last_sign:
        ans += 1
    last_sign = curr_sign

print(ans)