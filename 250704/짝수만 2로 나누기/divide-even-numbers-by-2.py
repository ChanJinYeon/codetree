from typing import List

n = int(input())
arr = list(map(int, input().split()))

# Please write your code here.
def func(arr: List[int]):
    for i in range(len(arr)):
        arr[i] = arr[i] // 2 if arr[i] % 2 == 0 else arr[i]

func(arr)
for i in arr:
    print(i, end=' ')
