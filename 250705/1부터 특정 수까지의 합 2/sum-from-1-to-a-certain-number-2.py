N = int(input())

# Please write your code here.
def func(N: int) -> int:
    if N == 1:
        return 1
    return N + func(N-1)

print(func(N))