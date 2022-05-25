#import library
from ast import literal_eval


import numpy as np
import pandas as pd

from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel, cosine_similarity



class ContentbasedModel:
    def __init__(self):
        pass

    def trainingDataBasesOnOverview(self,metadata):
        self.metadata = metadata
        metadata = self.dataCleansing()
        tfidf = TfidfVectorizer(stop_words = 'english',max_features=1000000)
        
        #Replace NaN with an empty string
        metadata['overview'] = metadata['overview'].fillna('')

        #Construct the required TF-IDF matrix by fitting and transforming the data
        tfidf_matrix = tfidf.fit_transform(metadata['overview'])

        cosine_sim = linear_kernel(tfidf_matrix[:31000], tfidf_matrix[:31000])
        return cosine_sim


    def trainingDataBasedOnGenres(self,metadata):
        self.metadata = metadata
        metadata = self.dataCleansing()
        metadata = metadata.apply(lambda metadata: self.cleanGenres(metadata), axis=1)
        
        count = CountVectorizer(stop_words='english')
        count_matrix = count.fit_transform(metadata['genres_soup'])

        cosine_sim = cosine_similarity(count_matrix[:31000], count_matrix[:31000])

        return cosine_sim,metadata
    
    def generateRecommendDataFrame(self,sim_scores,metadata):
        # sum = 0
        # for i in sim_scores:
        #     sum+=i[1]
        # print("Average accuray scoring of the 10 movies: ", str((sum/10)*100)[:6] , "%")

        # # Get the movie indices,score,title
        movie_indices = [i[0] for i in sim_scores]
        movie_score = [i[1] for i in sim_scores]
        *recommend_title, = metadata['title'].iloc[movie_indices]

        recommended_movies = []
        for i in range(len(movie_score)):
            recommended_movies.append([movie_indices[i],recommend_title[i],movie_score[i]])

        recommended_movies_df = pd.DataFrame(recommended_movies,columns=['id','title','accuracy_score'])
        return recommended_movies_df

    def getRecommendataionbasedOnGenres(self,movie_title,cosine_sim,data):
        metadata = data
        # metadata = metadata.apply(lambda metadata: self.cleanGenres(metadata), axis=1)

        # count = CountVectorizer(stop_words='english')
        # count_matrix = count.fit_transform(metadata['genres_soup'])

        # cosine_sim = cosine_similarity(count_matrix[:31000], count_matrix[:31000])

        # #Construct a reverse map of indices and movie titles
        indices = pd.Series(metadata.index, index=metadata['title']).drop_duplicates()

        title = movie_title

        # # Get the index of the movie that matches the title
        idx = indices[title]

        # # Get the pairwsie similarity scores of all movies with that movie
        sim_scores = list(enumerate(cosine_sim[idx]))
        # print(sim_scores[:10])

        # # Sort the movies based on the similarity scores
        # sim_scores = sorted(sim_scores.all(), key=lambda x: x[1], reverse=True)
        sim_scores.sort(key=lambda x: x[1].all(), reverse=True)

        # # Get the scores of the 10 most similar movies
        sim_scores = sim_scores[1:12]

        # # Return the top 10 most similar movies
        return self.generateRecommendDataFrame(sim_scores,metadata)



    def getRecommendationbasedOnOverview(self,movie_title,cosine_sim):
        metadata = self.dataCleansing()

        # tfidf = TfidfVectorizer(stop_words = 'english',max_features=1000000)
        
        # #Replace NaN with an empty string
        # metadata['overview'] = metadata['overview'].fillna('')

        # #Construct the required TF-IDF matrix by fitting and transforming the data
        # tfidf_matrix = tfidf.fit_transform(metadata['overview'])

        # cosine_sim = linear_kernel(tfidf_matrix[:33000], tfidf_matrix[:33000])

        # #Construct a reverse map of indices and movie titles
        indices = pd.Series(metadata.index, index=metadata['title']).drop_duplicates()

        title = movie_title

        # # Get the index of the movie that matches the title
        idx = indices[title]

        # # Get the pairwsie similarity scores of all movies with that movie
        sim_scores = list(enumerate(cosine_sim[idx]))

        # # Sort the movies based on the similarity scores
        sim_scores = sorted(sim_scores, key=lambda x: x[1].all(), reverse=True)

        # # Get the scores of the 10 most similar movies
        sim_scores = sim_scores[1:11]

        # # Return the top 10 most similar movies
        return self.generateRecommendDataFrame(sim_scores,metadata)

    def dataCleansing(self):
        metadata = self.metadata.copy()

        #drop unnecessary use column
        metadata.drop(
            labels=[
                'adult',
                'belongs_to_collection',
                'budget',
                #'genres',
                'homepage',
                #'id',
                'imdb_id',
                'original_language',
                'original_title',
                #'overview',
                'popularity',
                'poster_path',
                'production_companies',
                'production_countries',
                'release_date',
                'revenue',
                'runtime',
                'spoken_languages',
                'status',
                'tagline',
                # 'title',
                'video',
                'vote_average',
                'vote_count',
            ],
            axis=1,
            inplace=True
        )
        
        return metadata
    
    def cleanGenres(self,data: pd.Series):
        genres = data['genres']
        parsed_json = literal_eval(genres)
        genre_soup = " ".join(([i['name'].lower() for i in parsed_json]))
        data['genres_soup'] = genre_soup
        return data





