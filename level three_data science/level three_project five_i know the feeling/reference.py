# functions to use inside of kmeans.py


def makeLinesTuples(lines):
    '''Transforms a list of lines into a list of tuples. The values in each line must be delineated by " ". Each of
    those values will become a value in the tuple.'''
    # we will store our tuples in tuples
    tuples = []
    for line in lines:
        # split the line into a list based on " "
        values = line.split(" ")
        # convert each entry into the list into a float
        for i in range(1, len(values)):
            values[i] = float(values[i])
        # convert the list into a tuple
        vector_tuple = tuple(values)
        # add the tuple to tuples
        tuples.append(vector_tuple)
    print(f"Number of vectors: {len(tuples)}")
    print(f"Dimension of vector0: {len(tuples[0])}")
    return tuples


def makeCentroids(number_of_centroids=15, number_of_dimensions=301, spread=.5):
    '''Input the number of centroids you want and the number of dimensions they should have, including a dimension for the 
    label. Returns a dictionary of centroids. Each key in the dictionary corresponds to the label of the centroid. Each 
    centroid is stored as a tuple in the dictionary.'''
    from random import uniform
    # initialize centroid_counter so we can keep track of their labels
    centroid_counter = 0
    # initialize a dictionary that we will return
    centroid_dictionary = {}
    for i in range(number_of_centroids):
        # label the centroid using the counter
        centroid_label = f"Centroid {centroid_counter}"
        centroid_counter += 1
        # load the label into a list
        list = [centroid_label]
        # add number_of_dimensions - 1 random numbers between -1 and 1 to the list
        for j in range(number_of_dimensions - 1):
            list.append(uniform(-spread, spread))
        # convert the list into a tuple
        centroid = tuple(list)
        # add the tuple to our centroid dictionary
        centroid_dictionary[centroid_label] = centroid
    # return the centroid dictionary
    return centroid_dictionary


def makeDistanceDictionary(vector, centroid_dictionary):
    '''Given a vector and a centroid dictionary, this function will return a dictionary containing the distances
    between the vector and each of the centroids. Each key of the output dictionary is a centroid label, and its
    entry is the distance between the centroid and the vector.'''
    from math import sqrt
    distance_dictionary = {}
    for centroid_key in centroid_dictionary:
        centroid = centroid_dictionary[centroid_key]
        distance_squared = 0.0
        for i in range(1, len(centroid)):
            difference = vector[i] - centroid[i]
            distance_squared += difference * difference
        distance = sqrt(distance_squared)
        # load the distance into the corresponding key of the distance dictionary
        distance_dictionary[centroid_key] = distance
    # return distance_dictionary
    return distance_dictionary


def getClosestCentroid(distance_dictionary) -> str:
    '''Returns the centroid key corresponding to the smallest distance in distance_dictionary.'''
    return min(distance_dictionary, key=distance_dictionary.get)


def makeDictionaryOfLists(dictionary):
    '''Makes a dictionary copy with the same keys but filled with empty lists.'''
    output_dictionary = {}
    for key in dictionary:
        output_dictionary[key] = []
    return output_dictionary


def averageCluster(centroid_tuple, cluster_dictionary):
    '''Returns centroid_tuple if the cluster is empty. Returns a tuple. The first dimension of the tuple is the label of the centroid, and every other dimension
    are the actual coordinates of the centroid. The tuple is the average of the vectors in the centroid's cluster.'''
    # remember to account for empty clusters!
    centroid_label = centroid_tuple[0]
    print(f"Averaging cluster of {centroid_label}")
    # initialize our list of vectors
    vector_list = cluster_dictionary[centroid_label]
    print(f"{centroid_label} has {len(vector_list)} vectors in its cluster")
    # if our list of vectors is empty then return the input tuple:
    if vector_list == []:
        return centroid_tuple
    # initialize a list for us to store the final coordinates in
    coordinate_list = []
    for i in range(len(vector_list[0])):
        coordinate_list.append(0.0)
    # for each vector in the list:
    for vector in vector_list:
        # for each coordinate in the vector:
        for i in range(1, len(vector)):
            # add the coordinate to the matching dimension of our final list
            coordinate_list[i] = vector[i]
    # for each coordinate in our final list:
    for coordinate in coordinate_list:
        # divide the coordinate by the number of vectors we used
        coordinate = coordinate / len(vector_list)
    # prepend the centroid label to the list
    coordinate_list[0] = centroid_label
    # return the list as a tuple
    return tuple(coordinate_list)
