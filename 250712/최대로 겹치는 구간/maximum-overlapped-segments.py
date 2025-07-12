n = int(input())
segments = [tuple(map(int, input().split())) for _ in range(n)]

lst = [0 for _ in range(201)]

for a, b in segments:
    lst[a+100:b+100] = [x + 1 for x in lst[a+100:b+100]]

print(max(lst))