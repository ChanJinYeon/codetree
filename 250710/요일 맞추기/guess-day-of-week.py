m1, d1, m2, d2 = map(int, input().split())
date = ["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"]
month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

def calc(m: int, d: int) -> int:
    return sum(month[:m-1]) + d

calc_days = calc(m2, d2) - calc(m1, d1)
start_day = 1 # Mon

print(date[(calc_days + start_day + 7) % 7])