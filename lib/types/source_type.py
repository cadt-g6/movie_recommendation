

from enum import Enum


class SourceType(Enum):
    sample = "datasets/sample"
    original = "datasets/original"
    cleaned = "datasets/cleaned"
    v2 = "datasets/v2"