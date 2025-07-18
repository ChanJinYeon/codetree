N, K, P, T = map(int, input().split())  # N명, K 전염병 수명, P 개발자, T번 악수
handshakes = [tuple(map(int, input().split())) for _ in range(T)]
handshakes.sort(key=lambda T: T[0])

infected = [False] * (N+1)
cnt = [0] * (N+1)
infected[P] = True

for _, a, b in handshakes:
    ia, ib = infected[a], infected[b]
    if ia and cnt[a] < K:
        infected[b] = True
        cnt[a] += 1
    elif ib and cnt[b] < K:
        infected[a] = True
        cnt[b] += 1

print(''.join('1' if infected[i] else '0' for i in range(1, N+1)))