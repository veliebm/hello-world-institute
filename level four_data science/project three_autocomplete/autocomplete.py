"""
This program uses recursion to autocomplete any word or phrase you type into it. It bases its data
on the intrepid Reed Coke's search history.

Created 9/18/2020 by Ben Velie.
veliebm@gmail.com

"""

import trie

SEARCH_PATH = "my_history.txt"


def main():

    with open(SEARCH_PATH, "r", encoding="UTF-8") as search_file:
        contents = search_file.read()
        phrase_list = contents.splitlines()
        word_list = contents.replace("\n", "").split(" ")

if __name__ == "__main__":
    main()