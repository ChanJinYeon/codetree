n = int(input())
segments = [tuple(map(int, input().split())) for _ in range(n)]

lst = [0 for _ in range(100)]

for x1, x2 in segments:
    lst[x1:x2+1] = [x + 1 for x in lst[x1:x2+1]]

print(max(lst))