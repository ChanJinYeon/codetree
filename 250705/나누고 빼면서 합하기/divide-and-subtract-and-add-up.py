n, m = map(int, input().split())
A = list(map(int, input().split()))

# Please write your code here.
result = 0

while(m != 1):
    result += A[m - 1]
    m = m // 2 if m % 2 == 0 else m - 1

result += A[0]
print(result)