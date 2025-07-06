n, k, t = input().split()
n, k = int(n), int(k)
str = [input() for _ in range(n)]

# Please write your code here.
matches = [w for w in str if w.startswith(t)]
matches.sort()

print(matches[k-1])