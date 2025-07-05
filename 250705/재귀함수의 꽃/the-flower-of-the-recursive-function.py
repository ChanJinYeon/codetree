N = int(input())

# Please write your code here.
def func(N: int) -> None:
    if N == 0:
        return
    print(N, end=' ')
    func(N-1)
    print(N, end=' ')

func(N)