n = int(input())
students = [
    (h, w, i + 1)
    for i, (h, w) in enumerate([tuple(map(int, input().split())) for _ in range(n)])
]

students.sort(key=lambda x: (x[0], -x[1]))

for k in students:
    print(k[0], k[1], k[2])