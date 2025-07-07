user2_id, user2_level = input().split()
user2_level = int(user2_level)

# Please write your code here.
class User:
    def __init__(self, user_id = "codetree", level = 10):
        self.user_id = user_id
        self.level = level

    def print_user(self) -> None:
        print(f"user {self.user_id} lv {self.level}")

codetree = User()
test_user = User(user2_id, user2_level)

codetree.print_user()
test_user.print_user()