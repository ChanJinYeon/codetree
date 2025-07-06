from typing import List

n = int(input())
nums = list(map(int, input().split()))

# Please write your code here.
nums.sort()
maximum = 0
for i in range(n):
    get_maximum = nums[i]+nums[2*n - 1 - i]
    maximum = max(maximum,get_maximum)
print(maximum)
