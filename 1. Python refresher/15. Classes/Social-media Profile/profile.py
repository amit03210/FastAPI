class Profile:
    def __init__(self, username):
        self.username = username
        self.post_list = []

    def add_post(self, content):
        self.post_list.append(content)

    def __str__(self):
         if self.post_list:
            posts = "; ".join(self.post_list)
            return f"{self.username} has uploaded {len(self.post_list)} posts: {posts}"
         
         else:
            return f"{self.username} has uploaded no posts."

    