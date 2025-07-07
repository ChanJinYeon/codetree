MAX_N = 5

codenames = []
scores = []
for _ in range(MAX_N):
    codename, score = input().split()
    codenames.append(codename)
    scores.append(int(score))

# Please write your code here.
class Agent:
    def __init__(self, codename: str, score: int):
        self.codename = codename
        self.score = score
    
z = zip(codenames, scores)

agents = [ Agent(codename, score) for codename, score in z]
min_agent = min(agents, key=lambda obj: obj.score)
print(min_agent.codename, min_agent.score)