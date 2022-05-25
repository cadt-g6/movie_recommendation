#import library
import pandas as pd

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

class ReRankModel:
    def __init__(self, movie_title,data):
        self.movie_title = movie_title
        self.data = data

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
    
    def reRankBasedOnUserInterest(self):
        data = self.data

        count = CountVectorizer(stop_words='english')
        count_matrix = count.fit_transform(data['genres'])

        cosine_sim = cosine_similarity(count_matrix, count_matrix)

        # #Construct a reverse map of indices and movie titles
        indices = pd.Series(data.index, index=data['title']).drop_duplicates()
        # print(indices[:10])

        title = self.movie_title

        # # Get the index of the movie that matches the title
        idx = indices[title]

        # # Get the pairwsie similarity scores of all movies with that movie
        sim_scores = list(enumerate(cosine_sim[idx]))

        # # Sort the movies based on the similarity scores
        sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)

        # # Get the scores of the 10 most similar movies
        sim_scores = sim_scores[1:]

        # # Return the top 10 most similar movies
        return self.generateRecommendDataFrame(sim_scores,data)