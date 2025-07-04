n = int(input())
cnt = 0

# Please write your code here.
for i in range(n):
    for j in range(n):
        cnt = (cnt % 9) + 1
        print(cnt, end=' ')
    print()