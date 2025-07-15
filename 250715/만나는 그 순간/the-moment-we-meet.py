from typing import List, Iterator, Tuple

def position_generator(moves: List[Tuple[str, str]]) -> Iterator[int]:
    pos = 0
    for d, t_str in moves:
        t = int(t_str)
        step = 1 if d == 'R' else -1
        for _ in range(t):
            pos += step
            yield pos

n, m = map(int, input().split())
n_move = [tuple(input().split()) for _ in range(n)]
m_move = [tuple(input().split()) for _ in range(m)]

gen_n = position_generator(n_move)
gen_m = position_generator(m_move)

ans = -1
for i, (pos_n, pos_m) in enumerate(zip(gen_n, gen_m), start=1):
    if pos_n == pos_m:
        ans = i
        break
print(ans)