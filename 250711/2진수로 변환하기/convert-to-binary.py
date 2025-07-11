n = int(input())
l = []

if n == 0:
    print(0)
else:
    while n != 0:
        l.append(n % 2)
        n = n // 2
    print(*l[::-1], sep='')