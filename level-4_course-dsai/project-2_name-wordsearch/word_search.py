# This program generates a word search game for the user based off of the parameters they set in config.txt.
# First written by Benjamin Velie on June 21, 2020.
# Email him with any questions at veliebm@gmail.com.
import random
import copy


def main():
    # Open up the config file and store it as a list of lines.
    config_file = "config.txt"
    line_list = getLines(config_file)

    # Get our array size from the config file, then initialize the array with random characters.
    width = int(line_list[0])
    height = int(line_list[1])
    initialized_array = initializeArray(width, height)

    # Fill the array with the words that the user specifies in the config file.
    word_list = line_list[2:]
    word_search_array = makeSearch(initialized_array, word_list)

    # Format and print out the array.
    outputWordSearch(word_search_array)


def getLines(filename: str):
    '''Opens the target file, breaks it into a list of lines, then returns the list.'''
    with open(filename, "r") as target_file:
        print(f"Converted {filename} into a list.")
        return target_file.read().splitlines()


def initializeArray(width: int, height: int):
    '''Returns an array of the specified height and width containing random characters between A and Z.'''
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    initialized_array = []
    for column in range(width):
        initialized_array.append([])
        for row in range(height):
            initialized_array[column].append(random.choice(alphabet))
    print(f"Created array of width {width} and height {height}.")
    return initialized_array


def makeSearch(word_search_array, word_list):
    '''Returns a completed word search. Requires an array initialized with random letters and a list of words.'''

    # Loop through each word in the word list and attempt to place the word. Placed
    # characters will be tagged with @ so they don't get overwritten.
    for word in word_list:
        new_array = None
        while new_array is None:
            column, row = getRandomCoordinate(word_search_array)
            new_array = placeRandomDirection(
                word_search_array, word, column, row)
        word_search_array = new_array

    # Clean the array up by removing all tags from it.
    cleanWordSearch(word_search_array)

    return word_search_array


def cleanWordSearch(word_search_array):
    """Returns a word search with all the tags removed."""
    for column in range(len(word_search_array)):
        for row in range(len(word_search_array[column])):
            word_search_array[column][row] = word_search_array[column][row].replace("@", "")
    print("Cleaned word search.")
    return word_search_array


def getRandomCoordinate(word_search_array):
    """Returns a random x-coordinate and y-coordinate from the given array."""
    column = random.randint(0, len(word_search_array) - 1)
    row = random.randint(0, len(word_search_array[0]) - 1)
    return column, row


def reverseString(string: str) -> str:
    """Returns the reverse of the input string."""
    reversed_string = ""
    for character in string:
        reversed_string = character + reversed_string
    return reversed_string


def placeRandomDirection(word_search_array, word, column, row):
    """Returns an array with the word placed in a random direction at the coordinates. Returns None if it can't be placed."""
    if random.getrandbits(1) is 1:
        word = reverseString(word)
    print(f"Trying to place {word} at {column}, {row}:", end=" ")
    possible_directions = [placeDiagonalUp, placeDiagonalDown, placeHorizontal, placeVertical]
    new_array = random.choice(possible_directions)(
        word_search_array, word, column, row)
    return new_array


def placeDiagonalUp(word_search_array, word, column, row):
    """Returns an array with the word placed at the specified coordinates. Returns None if the word can't be placed."""
    new_array = copy.deepcopy(word_search_array)
    if column < len(word) - 1 and row >= len(word) - 1:
        for character in word:
            if notModified(new_array, column, row):
                print(f"Placing {character} at {column}, {row}")
                new_array[column][row] = character + "@"
                column += 1
                row -= 1
            else:
                print("Failed because word in way.")
                return None
        print(f"Success.")
        return new_array
    else:
        print(f"Failed because too near edge.")
        return None


def placeDiagonalDown(word_search_array, word, column, row):
    """Returns an array with the word placed at the specified coordinates. Returns None if the word can't be placed."""
    new_array = copy.deepcopy(word_search_array)
    if column >= len(word) - 1 and row >= len(word) - 1:
        for character in word:
            if notModified(new_array, column, row):
                print(f"Placing {character} at {column}, {row}")
                new_array[column][row] = character + "@"
                column -= 1
                row -= 1
            else:
                print("Failed because word in way.")
                return None
        print(f"Success.")
        return new_array
    else:
        print(f"Failed because too near edge.")
        return None


def placeHorizontal(word_search_array, word, column, row):
    """Returns an array with the word placed at the specified coordinates. Returns None if the word can't be placed."""
    new_array = copy.deepcopy(word_search_array)
    if column >= len(word) - 1:
        for character in word:
            if notModified(new_array, column, row):
                print(f"Placing {character} at {column}, {row}")
                new_array[column][row] = character + "@"
                column -= 1
            else:
                print("Failed because word in way.")
                return None
        print(f"Success.")
        return new_array
    else:
        print(f"Failed because too near edge.")
        return None


def placeVertical(word_search_array, word, column, row):
    """Returns an array with the word placed at the specified coordinates. Returns None if the word can't be placed."""
    new_array = copy.deepcopy(word_search_array)
    if row >= len(word) - 1:
        for character in word:
            if notModified(new_array, column, row):
                print(f"Placing {character} at {column}, {row}")
                new_array[column][row] = character + "@"
                row -= 1
            else:
                print("Failed because word in way.")
                return None
        print(f"Success.")
        return new_array
    else:
        print(f"Failed because too near edge.")
        return None


def notModified(word_search_array, column, row):
    """Returns true if the target member of the array hasn't been modified before."""
    if "@" in word_search_array[column][row]:
        return False
    else:
        return True


def outputWordSearch(word_search_array):
    """Prints out the word search. The word search must be cleaned of tags beforehand."""
    width = len(word_search_array)
    height = len(word_search_array[0])
    for row in range(height):
        for column in range(width):
            print(word_search_array[column][row], end=" ")
        print()


if __name__ == "__main__":
    main()
