N = int(input())

# Please write your code here.
def func(N: int) -> int:
    if N == 1:
        return 2
    if N == 2:
        return 4
    return func(N - 1) * func(N - 2) % 100

print(func(N))