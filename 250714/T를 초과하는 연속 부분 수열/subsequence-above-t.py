n, t = map(int, input().split())
arr = list(map(int, input().split()))

ans = 0
cnt = 0

for x in arr:
    if x > t:
        cnt += 1
    else:
        ans = max(ans, cnt)
        cnt = 0

ans = max(ans, cnt)
print(ans)