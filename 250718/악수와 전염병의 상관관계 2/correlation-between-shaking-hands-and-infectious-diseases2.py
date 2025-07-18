def infection(a: int, b: int, K: int) -> None:
    global dev
    if (dev[a] == 0 or dev[b] == 0) and 0 < dev[a] + dev[b] <= K:
        dev[a] += 1
        dev[b] += 1
    for i in range(1, len(dev)):
        dev[i] += 1 if dev[i] != 0 and not (i == a or i == b) else 0

N, K, P, T = map(int, input().split())  # N명, K 전염병 수명, P 개발자, T번 악수
handshakes = [tuple(map(int, input().split())) for _ in range(T)]
handshakes.sort(key=lambda T: T[0])

dev = [0 for _ in range(N+1)] # 값이 K가 되면 전염 X
dev[P] = 1

for p in handshakes:
    a, b = p[1], p[2]
    infection(a, b, K)

for i in range(1, len(dev)):
    print(1, end='') if dev[i] > 0 else print(0, end='')