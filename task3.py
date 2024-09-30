# Import necessary libraries
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Example movie-genre data
movies_data = {
    'Movie': ['Movie A', 'Movie B', 'Movie C', 'Movie D', 'Movie E'],
    'Genre': ['Action Adventure', 'Romance Drama', 'Action Sci-Fi', 'Drama Thriller', 'Sci-Fi Thriller']
}

# Create a DataFrame for movie-genre data
movies = pd.DataFrame(movies_data)

# Create a genre matrix using One-Hot Encoding
count_vectorizer = CountVectorizer(tokenizer=lambda x: x.split(' '))
genre_matrix = count_vectorizer.fit_transform(movies['Genre'])

# Convert to DataFrame for better visualization
genre_df = pd.DataFrame(genre_matrix.toarray(), index=movies['Movie'], columns=count_vectorizer.get_feature_names_out())
print(genre_df)

# Calculate cosine similarity between movies based on genres
movie_similarity = cosine_similarity(genre_matrix)

# Convert to DataFrame for better visualization
movie_similarity_df = pd.DataFrame(movie_similarity, index=movies['Movie'], columns=movies['Movie'])
print(movie_similarity_df)

# Function to recommend similar movies based on content similarity
def recommend_similar_movies(movie, movie_similarity_df, top_n=3):
    similar_movies = movie_similarity_df[movie].sort_values(ascending=False)[1:top_n+1]
    return similar_movies

# Recommend movies similar to 'Movie A'
similar_movies = recommend_similar_movies('Movie A', movie_similarity_df)
print(similar_movies)
