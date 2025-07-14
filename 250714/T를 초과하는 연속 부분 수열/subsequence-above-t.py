n, t = map(int, input().split())
arr = list(map(int, input().split()))

ans = 1
cnt = 1

for i in range(1, n):
    if arr[i] > arr[i-1] and arr[i] > t and arr[i-1] > t:
        cnt += 1
    else:
        ans = max(ans, cnt)
        cnt = 1
    
ans = max(ans, cnt)
print(ans)