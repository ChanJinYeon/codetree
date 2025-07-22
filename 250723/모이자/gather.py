import sys

INT_MAX = sys.maxsize

n = int(input())
A = list(map(int, input().split()))
len_A = len(A)

ans = INT_MAX
for i in range(len_A):
    tmp = 0
    for j in range(len_A):
        d = abs(i - j)
        tmp += d * A[j]
    ans = min(ans, tmp)
print(ans)