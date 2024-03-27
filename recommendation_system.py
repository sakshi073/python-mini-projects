from surprise import Dataset, Reader, KNNBasic
from surprise.model_selection import train_test_split
from surprise import accuracy

# Load the MovieLens 100k dataset (you can replace it with your own dataset)
data = Dataset.load_builtin('ml-100k')

# Define the reader to parse the dataset
reader = Reader(line_format='user item rating timestamp', sep='\t')

# Load the dataset (replace 'path/to/your/data' with the actual path to your dataset file)
data = Dataset.load_builtin('ml-100k', prompt=False)

# Split the data into train and test sets
trainset, testset = train_test_split(data, test_size=0.2, random_state=42)

# Use the KNNBasic collaborative filtering algorithm
sim_options = {'name': 'cosine', 'user_based': True}
model = KNNBasic(sim_options=sim_options)

# Train the model on the training set
model.fit(trainset)

# Make predictions on the test set
predictions = model.test(testset)

# Evaluate the model
accuracy.rmse(predictions)

# Function to get top N movie recommendations for a given user
def get_top_n_recommendations(predictions, n=10):
    top_n = {}
    for uid, iid, true_r, est, _ in predictions:
        if est > 3.5:  # Consider only high-rated predictions
            if uid not in top_n:
                top_n[uid] = []
            top_n[uid].append((iid, est))

    # Sort recommendations for each user based on estimated rating
    for uid, user_ratings in top_n.items():
        user_ratings.sort(key=lambda x: x[1], reverse=True)
        top_n[uid] = user_ratings[:n]

    return top_n

# Get top N movie recommendations for a user (replace 'user_id' with an actual user ID)
user_id = '1'
user_top_n = get_top_n_recommendations(predictions, n=5)[user_id]

# Print the top N movie recommendations for the user
print(f"Top 5 Movie Recommendations for User {user_id}:")
for movie_id, est_rating in user_top_n:
    print(f"Movie ID: {movie_id}, Estimated Rating: {est_rating}")
