import codecs
import sys
import operator

## use argument variables to allow you to pick the name of the book that you want
book_title = str(sys.argv[1])
print(f"Accessing {book_title}")

## open up the book and turn it into a string
file_object = codecs.open(book_title, 'r', encoding='utf8', errors='ignore')
book_string = file_object.read()
file_object.close()

## remove punctuation . , ! ? ' " from the string and lowercase it
book_string = book_string.lower()
# load our punctuation into a string
punctuation = ".,!?'\""
# go through each character of the punctuation string with a for loop and remove it from book_string
for punctuation_mark in punctuation:
    book_string = book_string.replace(punctuation_mark,"")
print("Stripped punctuation and made lowercase")

## split the string into a unigram array delimited by spaces
unigrams = book_string.split()

## use the unigram array to generate an array for bigrams, trigrams
bigrams = []
trigrams = []
unigrams_length = len(unigrams)
for i in range(unigrams_length):
    # add the word and the next word in the list to bigrams
    if i < unigrams_length - 1:
        bigram = "{} {}".format(unigrams[i], unigrams[i+1])
        bigrams.append(bigram)
    # add the word and the next two words in the list to trigrams
    if i < unigrams_length - 2:
        trigram = "{} {} {}".format(unigrams[i], unigrams[i+1], unigrams[i+2])
        trigrams.append(trigram)

## go through each element in our arrays and use a dictionary to count each unigrams, bigrams, trigrams
## we will write a method "grams_count()" that will use an array as an input and will output a dictionary with the grams counted
def grams_count(list_of_strings) -> dict:
    '''returns a dictionary where each string in the input list is mapped to the amount of times it occurs'''
    ## initialize output dictionary
    output_dictionary = {}

    ## use a for loop to go through each element of the list of strings
    for string in list_of_strings:

        ## check to see if the element is already in the dictionary. if it is, increment it. if it isn't, add it.
        if string in output_dictionary:
            output_dictionary[string] += 1
        else:
            output_dictionary[string] = 1

    ## return output dictionary
    return output_dictionary

unigrams_dictionary = grams_count(unigrams)
bigrams_dictionary = grams_count(bigrams)
trigrams_dictionary = grams_count(trigrams)

## sort each of our three dictionaries by count
sorted_unigrams_dictionary = sorted(unigrams_dictionary.items(), key=operator.itemgetter(1), reverse=True)
sorted_bigrams_dictionary = sorted(bigrams_dictionary.items(), key=operator.itemgetter(1), reverse=True)
sorted_trigrams_dictionary = sorted(trigrams_dictionary.items(), key=operator.itemgetter(1), reverse=True)

## output the top ten unigrams, bigrams, trigrams
# initializing list where we will put the top thirty tuples
top_thirty_list = []
# let's nest our for loops baby
# go through each of the three lists of tuples
for sorted_dictionary in [sorted_unigrams_dictionary, sorted_bigrams_dictionary, sorted_trigrams_dictionary]:
    if sorted_dictionary == sorted_unigrams_dictionary:
        print("Top ten unigrams:")
    elif sorted_dictionary == sorted_bigrams_dictionary:
        print("Top ten bigrams:")
    elif sorted_dictionary == sorted_trigrams_dictionary:
        print("Top ten trigrams:")
    # go through the first ten tuples in the list
    for i in range(10):
        # extract tuple from list
        tuple = sorted_dictionary[i]
        # add to a new list for when we output the top ten of each three
        top_thirty_list.append(tuple)
        # print the words and the words count from the tuple
        words = tuple[0]
        count = tuple[1]
        print(f"'{words}' {count}")

## to output the top ten n-grams of the three, sort/output top_thirty_list
print("Top ten n-grams:")
# Function to sort the list by second item of tuple 
def sort_tuple(tup):  
    # reverse = True (Sorts in descending order)  
    # key is set to sort using second element of  
    # sublist lambda has been used  
    return(sorted(tup, key = lambda x: x[1], reverse = True))   
# sort the list
sorted_top_thirty_list = sort_tuple(top_thirty_list)
# go through the top ten and print them out
for i in range(10):
    tuple = sorted_top_thirty_list[i]
    words = tuple[0]
    count = tuple[1]
    print(f"'{words}' {count}")