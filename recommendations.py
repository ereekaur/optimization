import numpy as np
import time

"""

@author Erno K
@date 2.2.2024

Movie recommendations for one user using cosine similarity and SVD.
Also extension into a LP-problem for multiple users and solving it with different methods shall be examined.
Preconditioner matrices and reorderings shall be considered e.g. McKee 

"""


users = 10000
movies = 1000

watched_matrix = np.random.choice([0, 1], size=(users, movies), p=[0.7, 0.3]) # sparsity


def cosine_similarity(vector1, vector2):

    dot_product = np.dot(vector1, vector2)
    norm_vector1 = np.linalg.norm(vector1)
    norm_vector2 = np.linalg.norm(vector2)
    similarity = dot_product / (norm_vector1 * norm_vector2)

    return similarity


def calculate_similarity_matrix(data):

    movies = data.shape[1] # get the number of columns of the matrix

    similarity_matrix = np.zeros((movies, movies))

    for i in range(movies):

        for j in range(movies):

            similarity_matrix[i, j] = cosine_similarity(data[:, i], data[:, j])

    return similarity_matrix


def movie_recommendations(watched_movies, similarity_matrix, n=5):
    
    watched_movie_similarity = similarity_matrix[:, watched_movies]
    mean_similarity = watched_movie_similarity.mean(axis=1)
    sorted_indices = np.argsort(mean_similarity)[::-1]
    recommended_movies = [movie for movie in sorted_indices if movie not in watched_movies]

    return recommended_movies[:n]



start_time = time.time()
movie_similarity = calculate_similarity_matrix(watched_matrix)
end_time = time.time()


user_id = 48  # for which user we want to recommend
user_watched_movies = np.where(watched_matrix[user_id] == 1)[0]

recommendations = movie_recommendations(user_watched_movies, movie_similarity)

print(f"\nUser {user_id} has watched: {user_watched_movies}")
print(f"Recommended movies: {recommendations}")
print(f"Calculation time: {end_time - start_time} seconds")
