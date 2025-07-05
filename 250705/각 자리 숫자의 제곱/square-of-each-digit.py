N = int(input())

# Please write your code here.
def func(N: int) -> int:
    if N == 0:
        return 0
    return (N % 10) ** 2 + func(N // 10)

print(func(N))