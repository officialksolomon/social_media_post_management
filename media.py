from dataclasses import dataclass
from typing import Protocol
from enum import Enum, auto


class MediaType(Enum):
    """Valid file types"""
    IMAGE = auto()
    VIDEO = auto()


class Media(Protocol):
    """Media Interface/protocols for MediaFiles"""

    type: MediaType
    path: str


@dataclass
class MediaFile:
    """Media file class"""
    type: MediaType
    path: str
