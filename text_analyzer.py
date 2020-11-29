# Author: Ryan Rochmanofenna
# Assignment #2 - TextAnalyzer
# Date due: 2020-10-09
# I pledge that I have completed this assignment without
# collaborating with anyone else, in conformance with the
# NYU School of Engineering Policies and Procedures on
# Academic Misconduct.

####### DO NOT EDIT FUNCTIONS BELOW ########

def character_is_digit(char):
    """Indicates whether the value referenced by char parameter
    is a digit character

    :param char: character to check
    :return: True when char is a digit character, False otherwise

    >>> test_char = 'b'
    >>> character_is_digit(test_char)
    False
    >>> test_char = '2'
    >>> character_is_digit(test_char)
    True
    """

    return char.isdigit()


def character_is_letter(char):
    """Indicates whether the value referenced by char parameter
    is a letter

    :param char: character to check
    :return: True when char is a letter, False otherwise

    >>> test_char = 'b'
    >>> character_is_letter(test_char)
    True
    >>> test_char = '2'
    >>> character_is_letter(test_char)
    False
    """

    return char.isalpha()

####### DO NOT EDIT FUNCTIONS ABOVE ########

def character_is_whitespace(char):
    if char == " " or char == "\n" or char == "\t":
        return True
    else:
        return False

def character_ends_sentence(char):
    if char == "." or char == "!" or char == "?":
        return True
    else:
        return False

def print_results(num_chars, num_spaces, num_digits, num_letters, num_sentences):

    print("""
Count of characters: {}
Count of spaces: {}
Count of digits: {}
Count of letters: {}
Count of sentences: {}\n""".format(num_chars,num_spaces,num_digits,num_letters,num_sentences))

def analyze_text():

    str_text = input("Please enter text to analyze (press ENTER/return without text to exit):")
    if str_text == "":
        return False
    else:
        chars = 0
        spaces = 0
        digits = 0
        letters = 0
        sentences = 0
        for character in str_text:
            chars += 1
            if character_is_digit(character):
                digits += 1
            if character_is_whitespace(character):
                spaces += 1
            if character_is_letter(character):
                letters += 1
            if character_ends_sentence(character):
                sentences += 1
        print_results(chars, spaces, digits, letters, sentences)
        return True

def run_text_analyzer():

    print("Welcome to the Text Analyzer!\n")
    quit = False
    while not quit:
        start_or_quit = analyze_text()
        if not start_or_quit:
            print("\nGoodbye!")
            quit = True

def main():
    """Runs a program for analyzing character counts from
    input text
    """

    # call run_text_analyzer() here and remove pass below
    run_text_analyzer()
    #pass


####### DO NOT REMOVE IF STATEMENT BELOW ########

if __name__ == '__main__':
    # Remove comments for next 4 lines to run doctests
    # print("Running doctests...")
    # import doctest
    # doctest.testmod(verbose=True)

    # print("\nRunning program...\n")

    main()

