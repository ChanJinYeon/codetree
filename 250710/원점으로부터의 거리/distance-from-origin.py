n = int(input())
points = [(int(i), tuple(map(int, input().split()))) for i in range(n)]

points.sort(key=lambda x: abs(x[1][0]) + abs(x[1][1]))

for point in points:
    print(point[0] + 1)