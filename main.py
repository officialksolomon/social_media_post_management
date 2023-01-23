from media import MediaFile, MediaType
from post import Post
from facebook import Facebook
from validators import get_factory


def main() -> None:
    """Sets up the everything and runs the program."""

    facebook = Facebook("Solomon", "132344")
    facebook.login()
    media = MediaFile(MediaType.IMAGE, "images\bg.png")
    post = Post("ChatGPT3", "ChatGPT has come to stay....", media)

    # print(post.media)
    if post.media is not None:
        validator = get_factory(post.media.type.name)
        facebook.publish(post, validator)
    facebook.publish(post)


if __name__ == "__main__":
    main()
