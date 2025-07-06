n = int(input())

# Please write your code here.
def func(N: int, cnt: int) -> int:
    if N == 1:
        return cnt
    return func(3 * N + 1, cnt + 1) if N % 2 == 1 else func(N // 2, cnt + 1)

print(func(n, 0))