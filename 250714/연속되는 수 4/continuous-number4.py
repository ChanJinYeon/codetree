n = int(input())
arr = [int(input()) for _ in range(n)]

cnt = 1
ans = 1

for i in range(1, n):
    if arr[i] > arr[i-1]:
        cnt += 1
    else:
        ans = max(ans, cnt)
        cnt = 1

ans = max(ans, cnt)
print(ans)
