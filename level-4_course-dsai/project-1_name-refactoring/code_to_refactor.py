from reference import *

# Get an ordered list of every word in the target file after stripping the punctuation.
target_filename = input("What file do you want to read? ")
word_list = getWordList(target_filename)

number_of_grams = int(input("How many grams do you want to see?"))
n = 4

print(f"Top {number_of_grams} n-grams:")
printGrams(makeAllGrams(word_list, n), 0, number_of_grams)

for i in range(1,n+1):
    print()
    print(f"Top {number_of_grams} {i}-grams:")
    printGrams(makeGram(word_list, i),0,number_of_grams)
