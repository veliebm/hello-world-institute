"""
This program uses recursion to autocomplete any word or phrase you type into it. It bases its data
on the intrepid Reed Coke's search history.

Created 9/18/2020 by Ben Velie.
veliebm@gmail.com

"""

from trie import Trie


SEARCH_PATH = "my_history.txt"

print(f"Accessing {SEARCH_PATH}...")

# Access the search history.
with open(SEARCH_PATH, "r", encoding="UTF-8") as search_file:
    contents = search_file.read().lower()

    for character in "!@#$%^&*(){}:\",.?<>/;[]\\-_=+":
        contents = contents.replace(character, "")

    phrase_list = [phrase.split() for phrase in contents.splitlines()]
    word_list = contents.split()

# Store the search history in Tries.
PHRASE_TRIE = Trie("!!PHRASES!!")
WORD_TRIE = Trie("!!WORDS!!")

for phrase in phrase_list:
    PHRASE_TRIE.store(phrase)

for word in word_list:
    WORD_TRIE.store(word)


def main():
    mode = int(input("Welcome to Ben's autocompleter!\nEnter 1 for word mode or 2 for phrase mode.\n>> "))
    
    while True:
        if mode == 1:
            input_word = input("Enter a part of a word. I'll finish it.\n>> ")
            rest_of_the_word = "".join((WORD_TRIE.unstore(input_word).autocomplete()))
            full_word = input_word + rest_of_the_word
            print(full_word)

        elif mode == 2:
            input_phrase = input("Enter part of a phrase. I'll finish it.\n>> ")
            rest_of_the_phrase = " ".join((PHRASE_TRIE.unstore([input_phrase]).autocomplete()))
            full_phrase = input_phrase + " " + rest_of_the_phrase
            print(full_phrase)

        else:
            raise RuntimeError("Whoah there! You can only pick 1 or 2!")


if __name__ == "__main__":
    main()
