class Score:
    def __init__(self, n: str, k: int, e: int, m: int):
        self.n, self.k, self.e, self.m = n, k, e, m

n = int(input())
scores = []

for _ in range(n):
    student_info = input().split()
    scores.append(
        Score(
            student_info[0],
            int(student_info[1]),
            int(student_info[2]),
            int(student_info[3])
            ))
    
scores.sort(key=lambda x: (-x.k, -x.e, -x.m))

for score in scores:
    print(score.n, score.k, score.e, score.m)