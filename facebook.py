from typing import Optional
from social_media import SocialMedia
from post import Post
from validators import Validator


class Facebook(SocialMedia):
    """Facebook social media platform"""

    def __init__(self, username: str, password: str) -> None:
        self.username = username
        self.password = password

    def publish(self, post: Post, validator: Optional[Validator] = None) -> None:
        """ publish post to Facebook"""

        # temporary implementation......
        if post.media and validator is not None:
            if validator.validate(post.media):
                print("")
                print("Valid file")
                print("Publishing new post....")
                print(f"Post title: {post.title}")
                print(f"Post content: {post.content}")
                print(f"Post mediafile: {post.media}")
            else:
                print("Invalid File, make changes and try again.")
