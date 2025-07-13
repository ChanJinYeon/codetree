n = int(input())
segments = [tuple(input().split()) for _ in range(n)]

idx = 1000
cnt = 0
lst = [0 for _ in range(2001)]

for a, b in segments:
    if b == 'L':
        lst[idx-int(a)+1:idx+1] = [x+1 for x in lst[idx-int(a):idx]]
    if b == 'R':
        lst[idx:idx+int(a)] = [x+1 for x in lst[idx:idx+int(a)]]
    
for i in lst:
    if i >= 2:
        cnt = cnt + 1

print(cnt)