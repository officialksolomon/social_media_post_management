from social_media import SocialMedia
from post import Post


class Facebook(SocialMedia):
    """Facebook social media platform"""

    def __init__(self, username: str, password: str) -> None:
        self.username = username
        self.password = password

    def publish(self, post: Post) -> None:
        """ publish post to Facebook"""

        # temporary implementation......
        print("Valid file")
        print("Publishing new post....")
        print(f"Post title: {post.title}")
        print(f"Post content: {post.content}")
        print(f"Post mediafile: {post.media}")
