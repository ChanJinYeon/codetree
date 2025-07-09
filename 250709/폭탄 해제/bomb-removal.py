unlock_code, wire_color, seconds = input().split()
seconds = int(seconds)

# Please write your code here.
class CCS:
    def __init__(self, code, color, second):
        self.code = code
        self.color = color
        self.second = second

ccs = CCS(unlock_code, wire_color, seconds)
print(f"code : {ccs.code}")
print(f"color : {ccs.color}")
print(f"second : {ccs.second}")