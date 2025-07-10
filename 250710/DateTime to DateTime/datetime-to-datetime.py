a, b, c = map(int, input().split())
day_to_minute = 24 * 60
hour_to_minute = 60

print((a-11)*day_to_minute + (b-11)*hour_to_minute + c-11)