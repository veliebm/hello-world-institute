### The purpose of this program is to create a personality quiz. It reads a formatted text file named quiz1.txt to get questions, 
### answers, and the personalities you can be matched with. When you answer a question, you earn a point toward one of the personalities. 
### Whichever personality has the most points by the end of the quiz is the one you get matched with.

## askQuestion() function is called for each question and returns the answer that the user selected
def askQuestion(lines: list) -> str:
    '''returns the answer that the user selected'''
    question = ""
    answers = []
    for line in lines:
        if containsQuestion(line):
            question = getArgument(line,1)
            break
    print(question)
    counter = 0
    for line in lines:
        if containsAnswer(line):
            counter += 1
            answer = getArgument(line,1)
            answers.append(answer)
            print(f"{counter}: {answer}")
    choice = int(input(">> "))
    print()
    return answers[choice-1]

## matchAnswer() inputs a list of lines and an answer choice and outputs the matching personality
def matchAnswer(lines: list, answer: str) -> str:
    '''inputs a list of lines and an answer choice and outputs the matching personality type'''
    ## increment through the list of lines and find which one contains the answer
    for line in lines:
        if getArgument(line,1) == answer:
            return getArgument(line,2)

## loadQuizFile() function takes a filename as an input, opens the file name, then returns the contents of the file 
## as a list of strings, with each string being a line of the file
def loadQuizFile(filename: str) -> list:
    '''opens a file and returns a list with each line as a string'''
    with open(filename, "r") as file:
        return file.read().splitlines()

## getArgument() grabs an argument in the line delineated by : and returns it
def getArgument(line: str, argument: int) -> str:
    '''grabs an argument in the line delineated by : and returns it'''
    arguments = line.split(":")
    return arguments[argument]

## containsResult() accepts a string as an input and returns true if it is coded to be a personality result
def containsResult(line: str) -> bool:
    '''accepts a string as an input and tells you if it is coded to be a personality result'''
    first_argument = getArgument(line, 0)
    if "result_" in first_argument:
        return True
    else:
        return False

## containsAnswer() accepts a string as an input and returns true if it is coded to be an answer choice
def containsAnswer(line: str) -> bool:
    '''accepts a string as an input and tells you if it is coded to be an answer choice'''
    first_argument = getArgument(line, 0)
    if containsResult(line):
        return False
    elif "a" in first_argument:
        return True
    else:
        return False

## containsQuestion() accepts a string as an input and tells you if it is coded to be a question
def containsQuestion(line: str) -> bool:
    '''accepts a string as an input and returns true if it is coded to be a question'''
    first_argument = getArgument(line, 0)
    if containsResult(line):
        return False
    elif "q" in first_argument:
        return True
    else:
        return False

## load our quiz file into a list of strings
filename = "quiz1.txt"
lines = loadQuizFile(filename)

## get title if it exists and set it as a variable
# initialize title variable
title = ""
# iterate through each line in the list
for line in lines:
    # if the line contains the title
    first_argument = getArgument(line, 0)
    if first_argument == "title":
        # set the title variable
        title = getArgument(line, 1)
        # exit the string
        break

## greet the user
print(title)
print()

## create a dictionary to keep score of each personality type
# initialize a dictionary of personality types
personalities = {}
# iterate through the list of lines again
for line in lines:
    # if the first argument contains "result_"
    first_argument = getArgument(line, 0)
    if containsResult(line):
        # remove "result_" from the first argument
        personality = first_argument.lstrip("result_")
        # add the remaining string to the dictionary along with the number zero
        personalities[personality] = 0

## iterate through the list of lines and check for whether the line contains a question
# question will store each question and its potential answers
question_and_answer_lines = []
for i in range(len(lines)):
    line = lines[i]

    ## determine which question and answers to send into the question and answer function
    # if there's a question in the line our question variable is already full then ship off the question variable and replace it
    if containsQuestion(line) or containsResult(line):
        if question_and_answer_lines != []:
            # asks a question and stores the answer as answer
            answer = askQuestion(question_and_answer_lines)
            # matches the answer to a personality
            personality = matchAnswer(question_and_answer_lines, answer)
            # increment corresponding personality
            personalities[personality] += 1
            # replace question_and_answer_lines with the new question
            question_and_answer_lines = [line]
            # if it's a result then break the loop so we can print our results
            if containsResult(line):
                break
        # elif question_and_answer_lines is empty then fill it with the new question
        elif question_and_answer_lines == []:
            question_and_answer_lines = [line]
    # elif the line contains an answer then add the answer to question_and_answer_lines
    elif containsAnswer(line):
        question_and_answer_lines.append(line)

## print the results
print("Here are your results!")
# start a counter to use for comparing the scores
highest_score = 0
# iterate through the personality types
for result in personalities:
    # if the personality has a higher score than the counter
    if personalities[result] > highest_score:
        # set the counter equal to that score
        highest_score = personalities[result]
# iterate through the personality types again
for result in personalities:
    # any personality that has the high score will be printed
    if personalities[result] == highest_score:
        for line in lines:
            if containsResult(line) and result in getArgument(line, 0):
                print("{}: {}".format(result, getArgument(line, 1)))

