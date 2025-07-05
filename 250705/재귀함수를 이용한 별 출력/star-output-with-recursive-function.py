n = int(input())

# Please write your code here.
def stars(N: int) -> None:
    if N == 0:
        return
    stars(N-1)
    print("*" * N)

stars(n)