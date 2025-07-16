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
max_len = max(len(n_lst), len(m_lst))
n_lst += [n_lst[-1]] * (max_len - len(n_lst))
m_lst += [m_lst[-1]] * (max_len - len(m_lst))

dev_lst = [n_lst[i] - m_lst[i] for i in range(max_len)]

ans = 0
last_sign = 0
    
for i in range(1, max_len):
    if n_lst[i] == m_lst[i] and n_lst[i-1] != m_lst[i-1]:
        ans += 1

print(ans)