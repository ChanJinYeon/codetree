m1, d1, m2, d2 = map(int, input().split())
num_of_days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
sum_days = [0]
# Please write your code here.
for i in range(len(num_of_days) - 1):
    sum_days.append(sum_days[i] + num_of_days[i + 1])

print(sum_days[m2-1] + d2 - sum_days[m1-1] - d1 + 1)