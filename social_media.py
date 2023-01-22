from abc import ABC, abstractmethod
from post import Post
from validators import Validator


class SocialMedia(ABC):
    """Social Media structure implemented by specific Social
    Media clients e.g Facebook, Instagram, Twitter"""

    # properties
    is_authenticated = False

    # Methods
    def login(self) -> None:
        self.is_authenticated = True
        print("User succesfully logged in...")

    @abstractmethod
    def publish(self, post: Post, validator: Validator) -> None:
        """Publish posts to social media plaform"""
        pass
