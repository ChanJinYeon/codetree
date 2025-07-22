a = input()
l = [c for c in a]

for i in range(len(l)):
    if l[i] == '0':
        l[i] = '1'
        break

b = ''.join(l)
print(int(b, 2))
