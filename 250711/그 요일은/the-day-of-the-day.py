m1, d1, m2, d2 = map(int, input().split())
A = input()

month = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
date = ["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"]
start_date = date.index("Mon")
target_date = date.index(A)
offset = (target_date - start_date + 7) % 7

def calc(m: int, d: int) -> int:
    return sum(month[:m-1]) + d

calc_day = calc(m2, d2) - calc(m1, d1) + 1

ans = (calc_day - offset -1) // 7 + 1
print(ans)
