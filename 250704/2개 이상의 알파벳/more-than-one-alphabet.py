A = input()
n = 0
# Please write your code here.
for i in range(len(A) - 1):
    n = n + 1 if A[i] != A[i + 1] else n

print("Yes" if n >= 2 else "No")