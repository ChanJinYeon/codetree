A = input()
len_A = len(A)
ans = 0
open_cnt = 0
for c in A:
    if c == '(':
        open_cnt += 1
    else:
        ans += open_cnt
print(ans)