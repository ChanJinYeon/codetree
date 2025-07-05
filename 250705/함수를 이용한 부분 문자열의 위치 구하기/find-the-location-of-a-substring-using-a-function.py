text = input()
pattern = input()

# Please write your code here.
def func():
    l = len(pattern)
    for i in range(len(text) - l + 1):
        if text[i:i+l] == pattern:
            return i
    return -1

print(func())