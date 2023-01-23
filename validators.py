from abc import ABC, abstractmethod
import re


class Validator(ABC):
    """Base interface for all validators"""

    @abstractmethod
    def validate(self, path: str) -> None:
        pass


class ImageValidator(Validator):
    """Validates image files"""
    __image_extensions = (".jpeg", ".jpg", ".png", ".gif", ".bmp", ".tiff")

    def validate(self, path: str) -> None:
        # regex = "([^\\s]+(\\.(?i)(jpe?g|png|gif|bmp))$)"
        regex = "(?i)([^\\s]+(\\.(jpe?g|png|gif|bmp))$)"
        pattern = re.compile(regex)
        if not re.search(pattern, path):
            raise Exception("Invalid image file.")


if __name__ == "__main__":
    img = ImageValidator()
    img.validate("example.jpg")
    # image_extensions = (".jpeg", ".jpg", ".png", ".gif", ".bmp", ".tiff")
    # print(r"\.(" + "|".join(image_extensions) + ")$")
