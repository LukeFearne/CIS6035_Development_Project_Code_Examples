# Sample data of how long people have watched certain adverts
advert_data = {
    "Advert1": [10, 15, 5, 20, 30],
    "Advert2": [5, 20, 30, 10, 25],
    "Advert3": [30, 10, 5, 15, 20]
}

# Function to recommend adverts based on how long people have watched them
def recommend_adverts(advert_data, threshold):
    recommended_adverts = []
    for advert in advert_data:
        avg_watch_time = sum(advert_data[advert])/len(advert_data[advert])
        if avg_watch_time > threshold:
            recommended_adverts.append(advert)
    return recommended_adverts

# Call the function with a threshold of 15 seconds
recommended_adverts = recommend_adverts(advert_data, 15)

# Print the recommended adverts
print("Recommended adverts: ", recommended_adverts)
