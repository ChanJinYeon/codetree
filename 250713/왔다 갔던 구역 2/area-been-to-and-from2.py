n = int(input())
segments = [tuple(input().split()) for _ in range(n)]

idx = 1000
cnt = 0
lst = [0 for _ in range(2001)]

for a_str, b in segments:
    a = int(a_str)
    if b == 'L':
        start = idx - a
        end = idx
        lst[start:end] = [x+1 for x in lst[start:end]]
        idx = start
    else:
        start = idx
        end = idx + a
        lst[start:end] = [x+1 for x in lst[start:end]]
        idx = end
    
for i in lst:
    if i >= 2:
        cnt = cnt + 1

print(cnt)