from enum import Enum


class DatasetType(Enum):
    credit = "credits.csv"
    keywords = "keywords.csv"
    links_small = "links_small.csv"
    links = "links.csv"
    movies_metadata = "movies_metadata.csv"
    ratings_small = "ratings_small.csv"
    ratings = "ratings.csv"

    def sample_path(self, prefix: str = "..") -> str:
        return prefix + "/" + "datasets/samples" + "/" + self.value

    def original_path(self, prefix: str = "..") -> str:
        return prefix + "/" + "datasets/original" + "/" + self.value

    def cleaned_path(self, prefix: str = "..") -> str:
        return prefix + "/" + "datasets/cleaned" + "/" + self.value

    # source: SourceType
    def path(self, source, prefix: str = "..") -> str:
        return prefix + "/" + source.value + "/" + self.value

    def values() -> list:
        return [path for path in DatasetType]
