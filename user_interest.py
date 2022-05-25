from lib.types.dataset_type import DatasetType
from lib.types.source_type import SourceType
from lib.utils.utils import print_dict
from lib.services.user_interest_service import UserInterestService
from models.reRank_model import reRank_model

import pandas as pd


def construct_genre(genre):
    return str(genre).lower().replace(" ", "")


def construct_genres_list(genres):
    return " ".join([construct_genre(genre) for genre in str(genres).split("|")])


service = UserInterestService(user_id=123963, source_prefix=".")
interest_dict = service.exec()

filtered_ratings = [construct_genre(genre)
           for genre, rating in interest_dict.items() if rating >= 3]
ranking_df = []
ranking_df.append([0, "Fake", " ".join(filtered_ratings)])

# search
for row in service.movies_df.sample(10).values:
    id = row[1]
    title = row[5]
    genres = construct_genres_list(row[9])
    ranking_df.append([id, title, genres])

df_to_rerank = pd.DataFrame(data=ranking_df, columns=["id", "title", "genres"])
model = reRank_model('Fake', df_to_rerank)

result_df = model.reRankBasedOnUserInterest()

print("\nUser interest genre:")
print_dict(filtered_ratings)

print("\nDataframe to rerank:")
print(df_to_rerank)

print("\nRanked dataframe:")
print(result_df)
