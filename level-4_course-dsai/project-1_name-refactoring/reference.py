# This file contains functions to be used in code_to_factor.py
from operator import itemgetter


def getWordList(target_filename: str):
    '''Opens target file, removes its punctuation, and returns it as a list of words in order.'''
    # opens the file as the string file_contents
    with open(target_filename, "r", encoding='utf8', errors="ignore") as target_file:
        file_contents = target_file.read()

    # removes the selected characters from our file string
    for character in '~!@#$%^&*()`,.<>/?\\|[]{};\':"':
        file_contents = file_contents.replace(character, '')

    return file_contents.lower().split()


def makeGram(word_list, n=1):
    '''Given a list of words and a integer, will output a dictionary of n-grams, n = the input integer.

    Each key of the dictionary is an individual n-gram. Each entry is the number of times that the n-gram
    appears in the list of words.'''

    ngram_dictionary = {}

    # Iterate through every word in the list. For each word, iterate through n words before it so we can build an n-gram for it.
    for i in range(len(word_list)):
        if i > n:

            # Get the n-gram with slicing. Adjust its count in the dictionary.
            ngram = " ".join(word_list[i-n:i])
            if ngram not in ngram_dictionary:
                ngram_dictionary[ngram] = 0
            ngram_dictionary[ngram] += 1

    # Sort the dictionary so the n-grams that occur the most are at the front.
    return sortDictionary(ngram_dictionary)


def makeAllGrams(word_list, n=1):
    '''Given a list of words and a integer, will output a dictionary of ALL n-grams up to n, n = the input integer.

    Each key of the dictionary is an individual n-gram. Each entry is the number of times that the n-gram
    appears in the list of words.'''
    ngram_dictionary = {}
    for i in range(0, n):
        ngram_dictionary.update(makeGram(word_list, i + 1))
    return ngram_dictionary


def sortDictionary(dictionary):
    '''Sorts the given dictionary such that the words that appear the most frequently are at the front.'''
    sorted_tuple_list = sorted(dictionary.items(), key=itemgetter(1), reverse=True)
    sorted_dictionary = dict(sorted_tuple_list)
    return sorted_dictionary

def printGrams(dictionary, start=0, end=1):
    '''Prints the specified range of grams from the dictionary.'''
    key_list = list(dictionary.keys())[start:end]
    for key in key_list:
        print(f"{key}: {dictionary[key]} repeats")