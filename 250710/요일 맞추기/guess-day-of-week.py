m1, d1, m2, d2 = map(int, input().split())
date = ["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"]
month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
sum_month = [0]
for i in range(len(month)-1):
    sum_month.append(sum_month[i] + month[i + 1])

# Please write your code here.
calc = month[m2-1] + d2 - month[m1-1] - d1 + 1
calc_date = (calc + 7) % 7

print(date[calc_date])