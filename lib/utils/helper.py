import pandas as pd


class Helper:
    def __init__(self) -> None:
        pass

    @staticmethod
    def find_all_genres(genres: pd.Series):
        genres = genres.str.split("|")
        genres_cleaned = [item for item in genres.to_list()
                        if isinstance(item, list)]

        all_movie_genres = "|".join([
            "|".join(i)
            for i in genres_cleaned
        ]).split("|")

        all_movie_genres = set(all_movie_genres)
        return list(all_movie_genres)