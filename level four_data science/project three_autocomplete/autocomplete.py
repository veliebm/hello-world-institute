# This is an autocomplete program. First, it asks you whether you want it to complete your words or you want it to complete
# your sentences. Then you input words or characters, and it prints a list of up to five autocomplete options or a message
# saying no results were found. To do this, it uses a data structure called a trie and a recursive
# function named autocomplete(). The dataset it uses is my_history.txt.
# First written on June 22, 2020 by Benjamin Velie (veliebm@gmail.com)

def main():
    ## Get the target file as a list of lines. Name it phrase list because each line is a phrase.
    dataset_name = "file1.txt"
    word_list_list = get_phrase_list(dataset_name)
    
    ## Convert the list of lines into a phrase trie, which we implement as a bunch of nested dictionaries.
    ## This will be used for our phrase autocomplete.
    phrase_trie = make_trie(word_list_list)
    print("Phrase trie constructed.")
    print(phrase_trie)

    ## Convert the list of lines into a massive list of words. Then, use the list of words
    ## to make a word trie for our character autocomplete.
    big_word_list = []
    for word_list in word_list_list:
        for word in word_list:
            big_word_list.append(word)
    word_trie = make_trie(big_word_list)
    print("Word trie constructed.")
    print(word_trie)

    ## Ask the user which autocomplete mode they want to activate.
    print("What do you want me to autocomplete?")
    print("(1) Words.")
    print("(2) Phrases.")
    settings_input = input(">> ")
    WORDS = False
    PHRASES = False
    if ("1" or "word") in settings_input.lower():
        WORDS = True
        print("Activating word mode.")
    if ("2" or "phrase") in settings_input.lower():
        PHRASES = True
        print("Activating phrase mode.")

    ## Use a while loop to keep asking the user for input until they type exit.
    ## Use autocomplete() to output the top five possible completions.
    while True:
        if WORDS:
            print("Enter some characters and I'll complete the rest.")
            user_input = input(">> ")
            autocomplete("")
        if PHRASES:
            print("Enter some words and I'll complete the rest.")



def make_trie(word_list_list: list) -> dict:
    """Given a list of word lists or strings, returns that list as a trie in the form of nested dictionaries."""
    root = {"value": "^ROOT^", "count": 0, "children": dict()}
    for word_list in word_list_list:
	    # Return the dictionary to the root level.
        current_dictionary = root
        # Increment root count.
        current_dictionary["count"] += 1
        for word in word_list:
            if word not in current_dictionary["children"]:
			    # Add the word to the current level's children.
                new_dictionary = {"value": word, "count": 0, "children": dict()}
                current_dictionary["children"][word] = new_dictionary
			# Set the dictionary equal to the word's level.
            current_dictionary = current_dictionary["children"][word]
			# Increment the count by one.
            current_dictionary["count"] += 1
	
    return root
        

def get_phrase_list(filename: str) -> list:
    """Returns the target file as a list of lists. Each sublist represents a line in the file broken into individual words."""
    with open(filename, "r", encoding="UTF-8") as file:
        line_list = file.read().splitlines()
        # Break each phrase in the list into a list of its words.
        phrase_list = []
        for line in line_list:
            words_in_phrase = line.split(" ")
            phrase_list.append(words_in_phrase)
        print(f"Imported {filename} and broke it up into words.")
    return phrase_list


def autocomplete():
    pass

if __name__ == "__main__":
    main()