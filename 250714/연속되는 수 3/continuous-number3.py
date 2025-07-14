N = int(input())
arr = [int(input()) for _ in range(N)]

cnt = 1
ans = 1

for i in range(1, N):
    if arr[i] > 0 and arr[i-1] > 0:
        cnt += 1
    elif arr[i] < 0 and arr[i-1] < 0:
        cnt += 1
    else:
        ans = max(cnt, ans)
        cnt = 1

ans = max(cnt, ans)
print(ans)