from abc import ABC, abstractmethod
from media import Media, MediaFile, MediaType
import re


class Validator(ABC):
    """Base interface for all validators"""

    @abstractmethod
    def validate(self, file: Media) -> bool:
        pass


class ValidatorFactory(ABC):
    """Represents a particular validator"""

    @abstractmethod
    def create_validator(self) -> Validator:
        pass


class ImageFactory(ValidatorFactory):

    def create_validator(self) -> Validator:
        return ImageValidator()


# class VideoFactory(ValidatorFactory):
#     def get_validator(self) -> Validator:
#         return VideoValidator()


class ImageValidator(Validator):
    """Validates image files"""
    __image_extensions = (".jpeg", ".jpg", ".png", ".gif", ".bmp", ".tiff")

    def validate(self, file: Media) -> bool:
        regex = regex = "([^\\s]+(\\.(?i)(jpe?g|png|gif|bmp))$)"
        pattern = re.compile(regex)
        if re.search(pattern, file.path):
            return True
        return False


FACTORIES = {
    "IMAGE": ImageFactory()
}

# functions


def get_factory(type: str) -> Validator:
    """factory method to get appropriated validator based on media type"""
    return FACTORIES[type].create_validator()


if __name__ == "__main__":
    img = ImageValidator()
    result = img.validate(
        MediaFile(MediaType.IMAGE, "example.jpg"))
    print(result)
    # image_extensions = (".jpeg", ".jpg", ".png", ".gif", ".bmp", ".tiff")
    # print(r"\.(" + "|".join(image_extensions) + ")$")
