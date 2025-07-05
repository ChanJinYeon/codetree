n = int(input())

# Please write your code here.
def pre(N: int) -> None:
    if N == 0:
        return
    print(N, end=" ")
    pre(N-1)

def post(N: int) -> None:
    if N == 0:
        return
    post(N-1)
    print(N, end=" ")

post(n)
print()
pre(n)