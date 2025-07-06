n = int(input())
arr = list(map(int, input().split()))

# Please write your code here.
for idx in range(0, n, 2):
    step_arr = arr[:idx + 1]
    step_arr.sort()
    print(step_arr[idx // 2], end=' ')