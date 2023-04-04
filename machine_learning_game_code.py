import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

# Sample user-item matrix
user_item_matrix = np.array([[5, 3, 0, 1],
                             [4, 0, 0, 1],
                             [1, 1, 0, 5],
                             [1, 0, 0, 4]])

# Compute cosine similarity matrix
similarity_matrix = cosine_similarity(user_item_matrix)

# Select a target user
target_user = 0

# Find similar users
similar_users = np.argsort(similarity_matrix[target_user])[::-1]

# Define number of items to recommend
num_items = 2

# Compute predicted ratings for all items
predicted_ratings = np.zeros(user_item_matrix.shape[1])
for item in range(user_item_matrix.shape[1]):
    if user_item_matrix[target_user, item] == 0:
        rating_sum = 0
        similarity_sum = 0
        for user in similar_users[1:]:
            if user_item_matrix[user, item] > 0:
                rating_sum += similarity_matrix[target_user, user] * user_item_matrix[user, item]
                similarity_sum += similarity_matrix[target_user, user]
        predicted_ratings[item] = rating_sum / similarity_sum

# Select top recommended items
recommended_items = np.argsort(predicted_ratings)[::-1][:num_items]

print("Recommended Items for User", target_user)
for item in recommended_items:
    print("Item", item)
