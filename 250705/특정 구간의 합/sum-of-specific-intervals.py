n, m = map(int, input().split())
arr = list(map(int, input().split()))
queries = [tuple(map(int, input().split())) for _ in range(m)]

# Please write your code here.
def func():
    global arr
    for i, j in queries:
        print(sum(arr[i-1:j]))

func()