n = int(input())
arr = list(map(int, input().split()))

# Please write your code here.
def gcd(a: int, b: int) -> int:
    return b if a % b == 0 else gcd(b, a % b)

def lcm (N: int, lcm_value: int) -> int:
    if N == 1:
        return lcm_value
    get_gcd = gcd(lcm_value, arr[N-2])
    get_lcm = lcm_value * arr[N-2] // get_gcd
    return lcm(N-1, get_lcm)

print(lcm(n, arr[n-1]))