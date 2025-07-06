N = int(input())

# Please write your code here.
def factorial(N: int) -> int:
    if N == 0:
        return 1
    if N == 1:
        return 1
    return N * factorial(N-1)

print(factorial(N))