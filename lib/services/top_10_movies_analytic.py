from lib.types.source_type import SourceType
from lib.types.dataset_type import DatasetType
from lib.services.seaborn_service import SeabornService

import pandas as pd


class Top10MoviesAnalystic:
    def __init__(self, data):
        self.movie_df = data

    def top_10_based_on_popularity(self):
        top_popular_movies = self.movie_df[:31000].sort_values(
            by=['popularity'], ascending=False)
        return top_popular_movies.head(1)['title'].to_list()

    def top_10_based_on_rating(self):
        top_avg_quan_movies = self.movie_df[:31000].sort_values(
            by=['avg_rating', 'quantity'], ascending=False)
        return top_avg_quan_movies.head(10)['title'].to_list()

    def top_10_based_on_revenue(self):
        top_revenue_movies = self.movie_df[:31000].sort_values(
            by=['revenue'], ascending=False)

        return top_revenue_movies.head(10)['title'].to_list()

    def top_10_based_on_profit(self):
        cleaned_budget_df = self.movie_df[:
                                          31000][self.movie_df["budget"] > 5000]
        cleaned_revenue_df = cleaned_budget_df[cleaned_budget_df['revenue'] != 0]

        profit_percentage = cleaned_revenue_df.assign(
            profit=lambda row: ((row['revenue'] - row['budget'])/row['budget'])*100)

        return profit_percentage.sort_values(
            by=['profit'], ascending=False).head(10)['title'].to_list()
