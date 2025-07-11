N, B = map(int, input().split())

def func(N: int, B: int) -> None:
    l = []
    if N == 0:
        print(0)
    else:
        while N != 0:
            l.append(N % B)
            N = N // B
        print(*l[::-1], sep='')
    
func(N, B)