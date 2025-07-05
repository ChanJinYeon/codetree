N = int(input())

# Please write your code here.
def func(N: int, cnt: int) -> int:
    if N == 1:
        return cnt
    return func(N // 2, cnt + 1) if N % 2 == 0 else func(N // 3, cnt + 1)

print(func(N, 0))