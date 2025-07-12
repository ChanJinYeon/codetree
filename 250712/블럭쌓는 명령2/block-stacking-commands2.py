n, k = map(int, input().split())
commands = [tuple(map(int, input().split())) for _ in range(k)]

l = [0 for _ in range(n + 1)]

for a, b in commands:
    l[a:b+1] = [x + 1 for x in l[a:b+1]]

print(max(l))