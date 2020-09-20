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
    contents = search_file.read()
    phrase_list = [phrase.split(" ") for phrase in contents.splitlines()]
    word_list = contents.replace("\n", "").split(" ")

# Store the search history in Tries.
PHRASE_TRIE = Trie("!!PHRASES!!")
WORD_TRIE = Trie("!!WORDS!!")

for phrase in phrase_list:
    PHRASE_TRIE.store(phrase)

for word in word_list:
    WORD_TRIE.store(word)


def main():
    mode = int(input("Welcome to Ben's autocompleter!\nEnter 1 for word mode or 2 for phrase mode.\n>> "))
    
    if mode == 1:
        input_word = input("Enter a part of a word. I'll finish it.\n>> ")

    if mode == 2:
        input_phrase = input("Enter part of a phrase. I'll finish it.\n>> ")


if __name__ == "__main__":
    main()