class Person:
    def __init__(self, n, s, r):
        self.n = n
        self.s = s
        self.r = r

n = int(input())
people = []

for _ in range(n):
    n_i, s_i, r_i = input().split()
    people.append(Person(n_i, s_i, r_i))

people.sort(key=lambda x: x.n)
print(f"name {people[n-1].n}")
print(f"addr {people[n-1].s}")
print(f"city {people[n-1].r}")