from typing import List

A = input()

# Please write your code here.
def isPalindrome(arr: str) -> bool:
    return A == A[::-1]

if (isPalindrome(A)):
    print("Yes")
else:
    print("No")