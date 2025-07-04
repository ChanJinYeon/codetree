n = int(input())
cnt = 0

# Please write your code here.
for i in range(4):
    for j in range(4):
        cnt = (cnt % 9) + 1
        print(cnt, end=' ')
    print()