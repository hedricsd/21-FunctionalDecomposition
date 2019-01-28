"""
Hangman.

Authors: Tristen Foisy, Sam Hedrick, Thomas Hoevener.
"""  # DONE: 1. PUT YOUR NAME IN THE ABOVE LINE.

# DONE: 2. Implement Hangman using your Iterative Enhancement Plan.

####### Do NOT attempt this assignment before class! #######

import random


def main():
    print("Game has started.")
    word = random_word()
    min_length = length()
    final_word = check_length(min_length, word)
    repeat_process(final_word)
    play_again()


def random_word():
    with open('words.txt') as f:
        f.readline()
        string = f.read()
        words = string.split()
    r = random.randrange(0, len(words))
    word = words[r]
    return word


def length():
    string = input('Input a length less than 23 for the secret word:')
    print()
    integer = int(string)
    return integer


def check_length(min_length, word):
    final_word = word
    while True:
        if len(final_word) < min_length:
            final_word = random_word()
        else:
            print('I am thinking of a word', len(final_word), 'letters long.')
            print()
            break
    return final_word


def guess_a_letter():
    letter = input('Guess a letter:')
    return letter


def check_guess(letter, final_word, number_wrong):
    for k in range(len(final_word)):
        if letter == final_word[k]:
            print('Correct!')
            print('Remaining incorrect guesses left:', 5 - number_wrong)
            return 'Correct!', k, letter
    print('Wrong!')
    print('Remaining incorrect guesses left:', 4 - number_wrong)
    return 'Wrong!', None, None


def repeat_process(final_word):
    number_wrong = 0
    constructed = []
    for k in range(len(final_word)):
        constructed = constructed + ['_']
    while True:
        letter = guess_a_letter()
        response, k, letter = check_guess(letter, final_word, number_wrong)
        building, correct = progress(final_word, letter, constructed)
        converter(building)
        message, number_wrong = end_game(building, correct, response, number_wrong)
        print(message)
        if message == 'You LOSE!':
            print('The correct answer was:', final_word)
            break
        elif message == 'You WIN!':
            break


def progress(final_word, letter, constructed):
    correct = []
    for k in range(len(final_word)):
        correct = correct + [final_word[k]]
    for j in range(len(final_word)):
        if letter == correct[j]:
            constructed[j] = letter
    return constructed, correct


def converter(constructed):
    x = ''
    for k in range(len(constructed)):
        x = x + constructed[k] + ' '
    print(x)


def check_if_win(constructed, correct):
    count = 0
    for k in range(len(constructed)):
        if constructed[k] == correct[k]:
            count = count + 1
    if count == len(correct):
        return True
    else:
        return False


def end_game(building, correct, response, number_wrong):
    message = ''
    if check_if_win(building, correct) is True:
        message = 'You WIN!'
    if response == 'Wrong!':
        number_wrong = number_wrong + 1
    if number_wrong == 5:
        message = 'You LOSE!'
    return message, number_wrong


def play_again():
    answer = input('Do you want to play again? (y/n)')
    print()
    if answer == 'y':
        print()
        print('#####################################')
        print()
        main()
    elif answer == 'n':
        print('Thanks for playing!')
    else:
        print("I SAID:")
        play_again()


main()