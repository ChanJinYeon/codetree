n, t = map(int, input().split())
arr = list(map(int, input().split()))

ans = 0
cnt = 1 if arr[0] > t else 0

for i in range(1, n):
    if arr[i] > arr[i-1] and arr[i] > t:
        cnt += 1
    else:
        ans = max(ans, cnt)
        cnt = 1 if arr[i] > t else 0
    
ans = max(ans, cnt)
print(ans)