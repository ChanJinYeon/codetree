m1, d1, m2, d2 = map(int, input().split())
A = input()

month = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
date = ["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"]
start_date = 0

def calc(m: int, d: int) -> int:
    return sum(month[:m-1]) + d

calc_day = calc(m2, d2) - calc(m1, d1)

for i in range(len(date)):
    if date[i] == A:
        start_date = i

ans = (calc_day + start_date) // 7
print(ans)
