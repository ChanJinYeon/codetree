from typing import List, Tuple, Iterator

def gen(move: List[Tuple[int, int]]) -> Iterator[int]:
    pos = 0
    for v, t in move:
        for _ in range(t):
            pos += v
            yield pos

n, m = map(int, input().split())

n_move = [tuple(map(int, input().split())) for _ in range(n)]
m_move = [tuple(map(int, input().split())) for _ in range(m)]

n_gen = gen(n_move)
m_gen = gen(m_move)

pos_n = pos_m = 0
n_end = m_end = False
last_sign = None
ans = 1

while not (n_end and m_end):
    if not n_end:
        try:
            pos_n = next(n_gen)
        except StopIteration:
            n_end = True
    if not m_end:
        try:
            pos_m = next(m_gen)
        except StopIteration:
            m_end = True
    
    diff = pos_n - pos_m

    if diff > 0:
        curr_sign = 1
    elif diff < 0:
        curr_sign = -1
    else:
        curr_sign = 0

    if last_sign == None:
        last_sign = curr_sign
    elif last_sign != curr_sign:
        last_sign = curr_sign
        ans += 1

print(ans)