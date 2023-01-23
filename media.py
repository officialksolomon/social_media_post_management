from dataclasses import dataclass
from typing import Protocol
from enum import Enum, auto

from validators import Validator


class MediaType(Enum):
    """Valid file types"""
    IMAGE = auto()
    VIDEO = auto()


class Media(Protocol):
    """Media Interface/protocols for MediaFiles"""
    type: MediaType
    path: str
    validator: Validator


@dataclass
class MediaFile:
    """Media file class"""
    type: MediaType
    path: str


@dataclass
class ImageFile:
    """Media file class"""
    type: MediaType
    path: str
    validator: Validator

    def __post_init__(self) -> None:
        self.validator.validate(self.path)
