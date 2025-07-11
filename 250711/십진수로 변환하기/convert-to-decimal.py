binary = int(input())

two = 1
ans = 0

while binary != 0:
    ans += (binary % 10) * two
    two *= 2
    binary = binary // 10

print(ans)