# This program groups emoji into 15 clusters via a process called k-means clustering. Some kind soul already sorted the emoji
# a little bit to start us off. She labeled each with a sprawling vector of 300 dimensions, which we'll use to sort our emoji further.
# We begin by randomly throwing 15 points within the 300-dimensional space made by the vectors. Each point will soon hatch
# into the center of a cluster of vectors, so we call the points centroids. Now that the centroids are scattered and ready,
# it's time to put them to work. Each vector in the dataset globs onto the nearest centroid, which leans into the sticky
# situation by leaping straight into the center of the cluster of vectors: we find its new position by averaging the
# coordinates of the entire cluster.
# Now that our centroid has moved, we need to pair it with a new vector cluster. Like before, chain each vector to the
# closest centroid, dub the group a cluster, then hurl the centroid into the center of the cluster. Repeat until the
# centroids won't budge. Now that you have your final clusters, gloriously output them to our anxiously awaiting user.
# contains the functions that we want to use
import reference
from csv import reader

# Open our text file and convert it into a list of lines. Each line contains a vector whose values are delineated by " ".
vector_file_name = "onlyemo_model_swm-300-3-3.w2v.txt"
with open(vector_file_name, "r") as vector_file:
    lines = vector_file.read().splitlines()
print(f"Imported vectors from {vector_file_name}")
# remove the first entry from lines because it just contains labels and no numerical data
lines.pop(0)

# Convert the list of lines into a list of tuples named vector_list. Each tuple should be a vector of 301 dimensions, but the
# first dimension just contains the label of what emoji it is, so we'll only use the other 300 for numerical data.
vector_list = reference.makeLinesTuples(lines)

# Randomly generate our centroids. Each centroid should be a tuple of 301 dimensions, and the first dimension should be a label.
# Store the centroids in a new dictionary named centroid_dictionary. Each key should correspond to the label of the centroid.
centroid_dictionary = reference.makeCentroids(15, 301)
print(f"Made {len(centroid_dictionary)} centroids")
print(f"Dimension of centroid 0: {len(centroid_dictionary['Centroid 0'])}")

# Create cluster_dictionary to store each list of vectors assigned to each centroid. The dictionary will have as many keys as
# there are centroids. Each key will be equal to the label of the centroid.
cluster_dictionary = reference.makeDictionaryOfLists(centroid_dictionary)

# Begin a while loop so our code will keep running until the centroids stop moving. Make a new Boolean, centroid_moved, to
# determine whether the centroid moved in the previous loop.
number_of_loops = 0
centroid_moved = True
while centroid_moved == True:

    # Set centroid_moved equal to false. Later, if the centroid moves during this loop, we will set it to true.
    centroid_moved = False

    # For each vector in the list of vectors, compute the distance between the vector and every centroid.
    # Store these values in a new dictionary named distance_dictionary. Each key in the dictionary should be the label of a centroid,
    # and each entry should be the distance between the vector and the centroid.
    distance_dictionary = {}
    cluster_dictionary = reference.makeDictionaryOfLists(centroid_dictionary)
    for vector in vector_list:
        distance_dictionary = reference.makeDistanceDictionary(
            vector, centroid_dictionary)

        # Add the vector to cluster_dictionary. It should be appended to the list corresponding to the
        # key of the centroid that the vector is closest to. Use distance_dictionary to do this.
        closest_centroid = reference.getClosestCentroid(distance_dictionary)
        cluster_dictionary[closest_centroid].append(vector)

    # Every centroid has now been assigned a cluster of vectors located in cluster_dictionary. It's time to move our
    # centroids. Average the cluster of each centroid using a for loop.
    for centroid_label in cluster_dictionary:
        current_coordinates = centroid_dictionary[centroid_label]
        new_coordinates = reference.averageCluster(
            current_coordinates, cluster_dictionary)

        # We must determine whether the centroid actually moves or not. If none of the centroids move, then we need to
        # exit our while loop. Use an if statement to check whether the new coordinates of the centroid don't equal the old
        # coordinates. If they are equal, set centroid_moved equal to true.
        if current_coordinates == new_coordinates:
            print(f"{centroid_label} did not move.")
        else:
            print(f"{centroid_label} moved.")
            centroid_moved = True

        # Now set the value of the centroid equal to the value of the average you just found.
        centroid_dictionary[centroid_label] = new_coordinates

    number_of_loops += 1

print(f"After {number_of_loops} iterations, all centroids have stopped moving")

# Now that the centroids have stopped moving, we need to output the final clusters we found. The first step is to
# load the file emoji_lookup.tsv into a new dictionary named emoji_dictionary. Each key of the dictionary
# should equal an emoji code, and each entry should equal its corresponding emoji.
emoji_dictionary = {}
emoji_filename = "emoji_lookup.tsv"
with open(emoji_filename, "r", encoding="UTF-8") as emoji_file:
    line_list = emoji_file.read().splitlines()
print(line_list)

# Each vector in cluster_dictionary has a label in its first dimension. This label corresponds to an emoji code key in
# emoji_dictionary. For each vector in cluster_dictionary, set it equal to corresponding emoji entry of emoji_dictionary. Store these in a
# new dictionary named output_dictionary. Each key should be the label of the corresponding centroid.
print(f"There are {len(cluster_dictionary)} clusters in cluster_dictionary.")
for vector_list_key in cluster_dictionary:
    print(
        f"Processing {len(cluster_dictionary[vector_list_key])} vectors in {vector_list_key}")
    for i in range(len(cluster_dictionary[vector_list_key])):
        vector = cluster_dictionary[vector_list_key][i]
        for line in line_list:
            if vector[0] in line:
                cluster_dictionary[vector_list_key][i] = line
        if not isinstance(vector, str):
            cluster_dictionary[vector_list_key][i] = line
for key in cluster_dictionary:
    list = cluster_dictionary[key]
    for i in range(len(list)):
        emoji_line = list[i]
        values = emoji_line.split("\t")
        cluster_dictionary[key][i] = values[1]

# Gloriously output our results! Each cluster should be printed separately.
print("Final results:")
print(" – – – – – – –")
for key in cluster_dictionary:
    print(f"{key}:")
    if len(cluster_dictionary[key]) > 0:
        for i in range(len(cluster_dictionary[key])):
            print(f"{cluster_dictionary[key][i]}", end=" ")
    print()
