a, b = map(int, input().split())
n = input()

def func(N: str, A: int, B: int) -> None:
    l = []
    trans_N = int(N, A)
    if N == 0:
        print(0)
    else:
        while trans_N != 0:
            l.append(trans_N % B)
            trans_N //= B
        print(*l[::-1], sep='')
        
func(n, a, b)