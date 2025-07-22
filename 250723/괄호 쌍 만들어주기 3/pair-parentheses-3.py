A = input()
len_A = len(A)
ans = 0
for i in range(len_A):
    if A[i] == '(':
        for j in range(i+1, len_A):
            if A[j] == ')':
                ans += 1

print(ans)