m1, d1, m2, d2 = map(int, input().split())
num_of_days = [0, 3, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
# Please write your code here.
print(sum(num_of_days[m1+1:m2+1])+d2-d1)