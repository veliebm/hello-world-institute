## initialize and load our dictionary with 5 french words
french_dictionary = {"the ocean":"la mer", "a pineapple":"un anana", "The cat":"Le chat", "a dog":"un chien", "France":"la France"}

## load our story into a string
story = "The cat walked to the ocean. There, he met a dog. They frolicked around until they stumbled on a pineapple in the sand. It contained a hidden message! They had to go to France."

## use string replacement to replace parts of our string with the corresponding dictionary entry
for word in french_dictionary:
    replacement_string = "{} ({})".format(french_dictionary[word], word)
    story = story.replace(word, replacement_string) 

## print our story then prints our edited story
print(story)