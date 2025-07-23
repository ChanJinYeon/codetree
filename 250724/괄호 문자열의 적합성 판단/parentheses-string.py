from collections import deque

s = input()
dq = deque()

for c in s:
    if c == '(':
        dq.append(c)
    elif c == ')':
        if dq:
            dq.pop()
        else:
            continue

print("Yes" if not dq else "No")