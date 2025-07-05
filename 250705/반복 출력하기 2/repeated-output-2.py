n = int(input())

# Please write your code here.
def printHelloWorld(N):
    if N == 0:
        return
    print("HelloWorld")
    return printHelloWorld(N-1)


printHelloWorld(n)