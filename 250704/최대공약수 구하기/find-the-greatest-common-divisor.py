n, m = map(int, input().split())

# Please write your code here.
def gcd(a: int,b: int) -> int:
    return b if a % b == 0 else gcd(b, a % b)

print(gcd(n, m))
