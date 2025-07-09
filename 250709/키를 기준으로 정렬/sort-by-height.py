class Person:
    def __init__(self, n, h, w):
        self.n = n
        self.h = h
        self.w = w

n = int(input())
people = []

for _ in range(n):
    n_i, h_i, w_i = input().split()
    people.append(Person(n_i, h_i, w_i))

people.sort(key=lambda x: x.h)

for i in range(n):
    print(people[i].n, people[i].h, people[i].w)