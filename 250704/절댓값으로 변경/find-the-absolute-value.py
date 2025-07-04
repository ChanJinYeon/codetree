n = int(input())
arr = list(map(int, input().split()))

# Please write your code here.
arr2 = [abs(i) for i in arr]
print(*arr2)