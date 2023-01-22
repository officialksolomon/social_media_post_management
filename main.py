from media import MediaFile, MediaType
from post import Post
from facebook import Facebook
from validators import get_factory


def main() -> None:
    """Sets up the everything and runs the program."""
    facebook = Facebook("Solomon", "132344")
    facebook.login()
    post = Post("ChatGPT3", "ChatGPT has come to stay....")
    media = MediaFile(MediaType.IMAGE, "images\bg.png")
    post.add_media(media)
    validator = get_factory(post.media.type.name)
    facebook.publish(post, validator)


if __name__ == "__main__":
    main()
