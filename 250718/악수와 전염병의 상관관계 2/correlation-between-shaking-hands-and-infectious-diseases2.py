def infection(a: int, b: int, K: int) -> None:
    global infected, cnt
    if infected[a] and cnt[a] < K:
        if not infected[b]:
            infected[b] = True
        cnt[a] += 1

N, K, P, T = map(int, input().split())  # N명, K 전염병 수명, P 개발자, T번 악수
handshakes = [tuple(map(int, input().split())) for _ in range(T)]
handshakes.sort(key=lambda T: T[0])

infected = [False] * (N+1)
cnt = [0] * (N+1)
infected[P] = True

for _, a, b in handshakes:
    infection(a, b, K)
    infection(b, a, K)

for i in range(1, len(infected)):
    print(1, end='') if infected[i] else print(0, end='')