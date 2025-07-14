n = int(input())
a = [int(input()) for _ in range(n)]

ans = 0
cnt = 0
for i in range(1, len(a)):
    if a[i] == a[i-1]:
        cnt += 1
    else:
        ans = max(ans, cnt+1)
        cnt = 0

print(ans)