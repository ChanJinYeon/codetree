a, b, c = map(int, input().split())
n = a * b * c
# Please write your code here.
def func(N: int, ans: int) -> int:
    if N == 0:
        return ans
    return func(N // 10, ans + N % 10)

print(func(n, 0))