secret_code, meeting_point, time = input().split()
time = int(time)

# Please write your code here.
class JamesBond:
    def __init__(self, secret, meeting, times):
        self.secret = secret
        self.meeting = meeting
        self.times = times

codetree = JamesBond(secret_code, meeting_point, time)
print(f"secret code : {codetree.secret}")
print(f"meeting point : {codetree.meeting}")
print(f"time : {codetree.times}")