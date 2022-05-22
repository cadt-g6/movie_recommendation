# import pandas as pd

# from lib.types.dataset_type import DatasetType
# from lib.types.source_type import SourceType

# TODO: COMPLETE THIS
# class UserInterestService:
#     def __init__(self, user_id, source_path: SourceType = SourceType.original) -> None:
#         self.user_id = user_id
#         self.source_path = source_path

#     def exec(self):
#         self.load_rating_df
#         self.load_movie_df
#         self.load_rating_by_user_df

#     def load_rating_df(self):
#         path = DatasetType.ratings.path(source=self.source_path)
#         self.rating_df = pd.read_csv(path)

#         self.rating_df.rename(
#             columns={'userId': 'user_id', 'movieId': 'movie_id'},
#             inplace=True
#         )

#     def load_movie_df(self):
#         path = DatasetType.movies_metadata.cleaned_path()
#         self.movies_df = pd.read_csv(path)
#         self.movies_df.rename(
#             columns={'id': 'movie_id'},
#             inplace=True
#         )

#     def load_rating_by_user_df(self):
#         self.rating_by_user: pd.DataFrame = self.rating_df[self.rating_df['user_id'] == self.user_id]
#         self.rating_by_user['movie_id'] = self.rating_by_user['movie_id'].astype(
#             str)
