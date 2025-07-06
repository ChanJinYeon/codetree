N = int(input())

# Please write your code here.
def func(N: int) -> int:
    if N == 1:
        return 1
    if N == 2:
        return 2
    return N + func(N-2)

print(func(N))