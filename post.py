from typing import Optional, Union
from dataclasses import dataclass
from media import Media


@dataclass
class Post:
    title: str
    content: str
    _media: Optional[Media] = None

    @property
    def media(self) -> Union[Media, None]:
        return self._media

    @media.setter
    def media(self, media: Media) -> None:
        self._media = media
