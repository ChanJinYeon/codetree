from collections import deque

s = input()
dq = deque()
valid = True

for c in s:
    if c == '(':
        dq.append(c)
    elif c == ')':
        if dq:
            dq.pop()
        else:
            valid = False
            break

print("Yes" if not dq and valid else "No")