from media import ImageFile, MediaType
from post import Post
from facebook import Facebook
from validators import ImageValidator


def main() -> None:
    """Sets up the everything and runs the program."""

    facebook = Facebook("Solomon", "132344")
    facebook.login()
    image = ImageFile(MediaType.IMAGE, "images\bg.png", ImageValidator())
    post = Post("ChatGPT3", "ChatGPT has come to stay....", image)
    facebook.publish(post)


if __name__ == "__main__":
    main()
