from typing import List

n, m = map(int, input().split())

n_move = [tuple(input().split()) for _ in range(n)]
m_move = [tuple(input().split()) for _ in range(m)]

n_lst = [0]
m_lst = [0]

def func(N: int, move: List, lst: List) -> None:
    for i in range(N):
        d, t_str = move[i]
        t = int(t_str)
        k = lst[-1]
        for j in range(1, t+1):
            lst.append(k + j) if d == 'R' else lst.append(k - j)

func(n, n_move, n_lst)
func(m, m_move, m_lst)

ans = -1
for i in range(1, len(min(n_lst, m_lst))):
    if n_lst[i] == m_lst[i]:
        ans = i
        break
print(ans)