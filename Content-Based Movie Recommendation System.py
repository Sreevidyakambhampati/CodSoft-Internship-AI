import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Sample movie dataset with genre
movies_data = {
    'Movie': ['Movie A', 'Movie B', 'Movie C', 'Movie D', 'Movie E'],
    'Genre': ['Action Adventure', 'Romance Drama', 'Action Sci-Fi', 'Drama Thriller', 'Sci-Fi Thriller']
}

# Convert to DataFrame
movies = pd.DataFrame(movies_data)

# Clean genres (lowercase, stripped)
movies['Genre'] = movies['Genre'].str.lower().str.strip()

# Use TF-IDF Vectorizer instead of CountVectorizer
tfidf = TfidfVectorizer(tokenizer=lambda x: x.split())
genre_matrix = tfidf.fit_transform(movies['Genre'])

# Compute cosine similarity
cosine_sim = cosine_similarity(genre_matrix)

# Convert to DataFrame
similarity_df = pd.DataFrame(cosine_sim, index=movies['Movie'], columns=movies['Movie'])

# Improved recommendation function
def recommend_similar_movies(movie_title, similarity_df, top_n=3):
    movie_title = movie_title.title()  # normalize input
    if movie_title not in similarity_df:
        return f"'{movie_title}' not found in the movie database."

    similar_scores = similarity_df[movie_title].sort_values(ascending=False)[1:top_n+1]
    return list(similar_scores.index)

# Example usage
print("Top 3 recommendations for 'Movie A':")
print(recommend_similar_movies('movie a', similarity_df))
