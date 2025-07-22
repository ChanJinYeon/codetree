a = input()
max_val = int(a, 2)

for i in range(len(a)):
    l = list(a)
    l[i] = '1' if l[i] == '0' else '0'
    b = ''.join(l)
    max_val = max(max_val, int(b, 2))

print(max_val)
