class rule:
    def __init__(self, number):
        self.number = number
        self.followerList = []
        self.followingList = []
    def add_follower(self, new_follower):
        self.followerList.append(new_follower)
    def start_following(self, number_to_follow):
        self.followingList.append(number_to_follow)
    def presentNumber(self):
        print(f"{self.followingList} <- {self.number} <- {self.followerList}")