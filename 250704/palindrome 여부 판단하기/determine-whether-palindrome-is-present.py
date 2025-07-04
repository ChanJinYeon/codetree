from typing import List

A = input()

# Please write your code here.
def isPalindrome(arr: str) -> bool:
    return A == A[::-1]

print("Yes" if isPalindrome(A) else "No")