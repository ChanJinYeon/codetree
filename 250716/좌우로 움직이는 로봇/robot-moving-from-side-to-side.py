from typing import List, Tuple, Iterator

def pos(move: List[Tuple[int, int]]) -> Iterator[int]:
    pos = 0
    for m_str, d in move:
        m = int(m_str)
        step = 1 if d == 'R' else -1
        for _ in range(m):
            pos += step
            yield pos        
    
n, m = map(int, input().split())
n_move = [tuple(input().split()) for _ in range(n)]
m_move = [tuple(input().split()) for _ in range(m)]

n_gen = pos(n_move)
m_gen = pos(m_move)

ans = 0
pos_n = pos_m = 0
last_equal = True
done_n = done_m = False

while not(done_n and done_m):
    if not done_n:
        try:
            pos_n = next(n_gen)
        except StopIteration:
            done_n = True
    if not done_m:
        try:
            pos_m = next(m_gen)
        except StopIteration:
            done_m = True
    if not last_equal and pos_n == pos_m:
        ans += 1
    last_equal = (pos_n == pos_m)

print(ans)