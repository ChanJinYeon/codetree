n = int(input())
l = []
while n != 0:
    l.insert(0, n % 2)
    n = n // 2
print(*l, sep='')