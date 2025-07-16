N, M, K = map(int, input().split())
student = [0 for _ in range(N+1)]

for _ in range(M):
    penalty = int(input())
    student[penalty] += 1
    if student[penalty] >= K:
        print(penalty)
        break
