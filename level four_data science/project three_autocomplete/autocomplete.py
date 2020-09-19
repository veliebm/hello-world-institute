"""
This program uses recursion to autocomplete any word or phrase you type into it. It bases its data
on the intrepid Reed Coke's search history.

Created 9/18/2020 by Ben Velie.
veliebm@gmail.com

"""

from trie import Trie

SEARCH_PATH = "my_history.txt"


def main():

    with open(SEARCH_PATH, "r", encoding="UTF-8") as search_file:
        contents = search_file.read()
        phrase_list = [phrase.split(" ") for phrase in contents.splitlines()]
        word_list = contents.replace("\n", "").split(" ")

    phrase_trie = Trie("!!PHRASES!!")
    word_trie = Trie("!!WORDS!!")

    for phrase in phrase_list:
        phrase_trie.store(phrase)

    for word in word_list:
        word_trie.store(word)


if __name__ == "__main__":
    main()