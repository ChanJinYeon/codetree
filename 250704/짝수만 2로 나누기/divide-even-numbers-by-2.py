n = int(input())
arr = list(map(int, input().split()))

arr2 = [i//2 if i%2==0 else i for i in arr]

print(*arr2)