import string
from random import choice

word_set = {'python', 'java', 'kotlin', 'javascript'}
lives = 8


def hide_word(word, letter_set):
    '''
    Returns a string with hidden letters that are not in the set but are in the word.

    Example:  letter_set = {a, o , p, w}'; word = 'apple' ; return 'app--'
    '''
    return ''.join([letter if letter in letter_set else '-' for letter in word])


def check_input(input_string, letter_set):
    '''Return True if the input data is valid.'''

    # Check length of str
    if len(input_string) != 1:
        print('You should input a single letter')
        return False
    # Check for a lowercase letter.
    if input_string not in string.ascii_lowercase:
        print('Please enter a lowercase English letter')
        return False
    # Check for unique letter
    if input_string in letter_set:
        print("You've already guessed this letter")
        return False

    return True


def game(lives):
    '''Body of game'''
    choice_word = choice(tuple(word_set))  # get random word
    letter_set = set()

    while lives != 0 and not set(choice_word).issubset(letter_set):
        hidden_word = hide_word(word=choice_word, letter_set=letter_set)
        print(f'\n{hidden_word}')

        letter = input('Input a letter:')
        if not check_input(input_string=letter, letter_set=letter_set):
            continue

        if letter not in choice_word:
            print("That letter doesn't appear in the word")
            lives -= 1

        letter_set.add(letter)

    if lives != 0:
        print(choice_word)
        print('You guessed the word!')
        print('You survived!')
    else:
        print('You lost!')


print('H A N G M A N')
while True:
    status = input('Type "play" to play the game, "exit" to quit:')
    if status == 'exit':
        break
    elif status == 'play':
        game(lives=lives)
    else:
        continue