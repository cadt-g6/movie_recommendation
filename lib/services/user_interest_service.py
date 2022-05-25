import pandas as pd

from lib.utils.helper import Helper
from lib.types.dataset_type import DatasetType
from lib.types.source_type import SourceType


class UserInterestService:
    def __init__(self, user_id: int, source_path: SourceType = SourceType.original, source_prefix: str = ".") -> None:
        self.user_id = user_id
        self.source_path = source_path
        self.source_prefix = source_prefix

    def exec(self):
        movies_df = self.fetch_movie_df()
        rating_df = self.fetch_rating_df()
        
        rating_per_user_df = self.fetch_rating_per_user_df(
            self.user_id, rating_df)
        movies_per_user_df = self.fetch_movies_per_user_df(
            rating_per_user_df, movies_df)
        avg_rating_dict = self.fetch_avg_rating_dict(movies_per_user_df)
        
        return avg_rating_dict

    def fetch_movie_df(self) -> pd.DataFrame:
        movies_df = pd.read_csv(
            DatasetType.movies_metadata.cleaned_path(prefix=self.source_prefix))
        movies_df.rename(
            columns={'id': 'movie_id'},
            inplace=True
        )
        return movies_df

    def fetch_rating_df(self) -> pd.DataFrame:
        rating_df = pd.read_csv(DatasetType.ratings.path(
            source=self.source_path, prefix=self.source_prefix))

        rating_df.rename(
            columns={'userId': 'user_id', 'movieId': 'movie_id'},
            inplace=True
        )

        return rating_df

    def fetch_rating_per_user_df(
        self,
        user_id: int,
        rating_df: pd.DataFrame
    ):

        rating_per_user_df = rating_df[rating_df['user_id'] == user_id]
        rating_per_user_df['movie_id'] = rating_per_user_df['movie_id'].astype(
            str)

        return rating_per_user_df

    def fetch_movies_per_user_df(
        self,
        rating_per_user_df: pd.DataFrame,
        movies_df: pd.DataFrame
    ):
        movies_per_user_df = pd.merge(
            left=rating_per_user_df,
            right=movies_df,
            on='movie_id'
        )
        return movies_per_user_df

    def fetch_avg_rating_dict(self, input_movies_df: pd.DataFrame) -> dict:
        rating_dict = {}
        avg_rating_dict = {}

        for row in input_movies_df.values:
            # movie_id = row[1]
            rating = row[2]
            genres = row[12]

            for genre in str(genres).split("|"):
                if(rating_dict.get(genre) == None):
                    rating_dict[genre] = []
                rating_dict[genre].append(rating)

        for key, value in rating_dict.items():
            avg_rating_dict[key] = sum(value) / len(value)

        dict_sorted = sorted(
            avg_rating_dict.items(),
            key=lambda element: element[1],
            reverse=True,
        )

        avg_rating_dict = {key: value for key, value in dict_sorted}
        return avg_rating_dict
