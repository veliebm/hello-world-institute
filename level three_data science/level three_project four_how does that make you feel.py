### This program, Eliza, imitates a therapist. When the program starts, she greets you and asks you how you feel.
### After you respond, she references reference.py to decide what to say next. This conversational dance continues
### until the user asks to quit, presumably to live the rest of his life unburdened by mental illness. Let's get to it!
import re
import reference
import random
def main():
    ## (1) greet the user and ask them how they are
    print("Hey there, I'm Eliza. How are you feeling today?")

    ## (2) use while loop so user stays in the program until they enter quit
    while True:

        ## (3) get user response and remove '.' and '!' from their response
        user_input = input(">> ")
        modified_user_input = removeCharacters(user_input,".!")
        # end the conversation if the user types quit
        if modified_user_input.lower() == "quit":
            break
                
        ## (4) use re.search() to see if any of the patterns are in reference.psychobabble_patterns 
        ## match the user response (must be in a function)
        pattern, pattern_match_object = patternMatch(modified_user_input)

        ## (5) pick a random response from reference.psychobabble_responses 
        ## based on which pattern matched in step 4 (must be in a function)
        ## the function you write to pick a random response must use the reference.format_response() function to format the response
        response = getResponse(pattern, pattern_match_object)
        print(response)

    ## (6) say goodbye to the user
    print("I'm here anytime you need me. Take care.")

def getResponse(pattern: str, pattern_match_object) -> str:
    '''pick a random response from reference.psychobabble_responses matching the input pattern and associated match object.
    uses reference.format_response() to format the response'''
    # get a list of possible responses
    possible_responses = reference.psychobabble_responses[pattern]
    # randomly pick one of the responses
    unformatted_response = random.choice(possible_responses)
    # properly format the response
    formatted_response = reference.format_response(pattern_match_object, unformatted_response)
    return formatted_response

## patternMatch() must return the first key from the dictionary whose pattern was a match,
## and the MatchObject resulting from re.match()
def patternMatch(string):
    '''searches reference.psychobabble_patterns for the input string and returns the first key from
    the dictionary whose pattern is a match and the corresponding MatchObject'''
    for key in reference.psychobabble_patterns:
        # call re.search() to see if the dictionary entry regex matches string
        regex = reference.psychobabble_patterns[key]
        match = re.search(regex, string)
        # if we find a match, return the key and the match object we generated
        if match:
            return key, match

def removeCharacters(string: str, characters: str) -> str:
    '''removes the target characters from the target string. removeCharacters("hello.","l.")
    should return "heo"'''
    # iterate through each character in characters
    for character in characters:
        # for each character, replace that character in string with ""
        string = string.replace(character, "")
    return string

main()