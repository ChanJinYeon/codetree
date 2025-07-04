A = input()
n = 0
# Please write your code here.
def func(s: str) -> bool:
    for i in range(len(s)):
        if s[i] != s[0]:
            return True
    return False

print("Yes" if func(A) else "No")