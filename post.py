from dataclasses import dataclass
from media import Media


@dataclass
class Post:
    title: str
    content: str
    # media: Media

    def add_media(self, media: Media) -> None:
        self._media: Media = media

    @property
    def media(self) -> Media:
        return self._media

    @media.setter
    def media(self, media: Media) -> None:
        self._media = media
