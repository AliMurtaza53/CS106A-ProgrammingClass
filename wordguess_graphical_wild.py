"""
File: word_guess.py
-------------------
Play WordGuess!
The computer first selects a secret word at random from
a list built into the program. The program then prints out a row of dashes— one for each
letter in the secret word and asks the user to guess a letter. If the user guesses a letter that
is in the word, the word is redisplayed with all instances of that letter shown in the correct
positions, along with any letters correctly guessed on previous turns. If the letter does not
appear in the word, the user is charged with an incorrect guess. The user keeps guessing
letters until either (1) the user has correctly guessed all the letters in the word or (2) the
user has made eight incorrect guesses.
"""

import random
import tkinter
from tkinter import *
import time


LEXICON_FILE = "Lexicon.txt"    # File to read word list from
INITIAL_GUESSES = 8             # Initial number of guesses player starts with

# for graphics
CANVAS_WIDTH = 1200      # Width of drawing canvas in pixels
CANVAS_HEIGHT = 800     # Height of drawing canvas in pixels
CHANGE_X_START = 10
CHANGE_Y_START = 7
DASH_SIZE = 10
WRD_SIZE = 50
TIME_SIZE = 50



def play_game(secret_word, canvas):
    '''
    String -> String
    input: str secret_word
    output: str result of game
    the function takes a word and enables the user to play WordGuess as described in file summary above
    '''

    # start with initial guesses
    guesses_left = INITIAL_GUESSES
    # start with dashes for the word
    current_guess = "-" * len(secret_word)
    # could try "- " * (len(secret_word) - 1) + "-"

    # for loop to keep track of guesses:
    while guesses_left > 0:

        # try update
        canvas.update()

        # print status
        print_status(current_guess, guesses_left, canvas)


        # prompt for input
        canvas.create_text(1 / 4 * CANVAS_WIDTH, 1/4 * CANVAS_HEIGHT, anchor='center', font='Gothic 40',
                           text="Type a single letter here, then press enter")
        input_letter = input()

        # check if input_letter in secret_word
        if input_letter.lower() in secret_word.lower():
            # print success
            # canvas.create_text(1 / 4 * CANVAS_WIDTH, 1 / 4 * CANVAS_HEIGHT, anchor='center', font='Gothic 40',
            #                   text="That guess ")

            # find the index(es) where input letter can be found in the word and create a list of it
            ind_letter_in_word = list(indexes(secret_word, input_letter))

            # update current word by replacing the letters in this index(es) with input letter
            current_guess = update_word(current_guess, input_letter, ind_letter_in_word)

        else:
            canvas.create_text(1 / 4 * CANVAS_WIDTH, 1 / 4 * CANVAS_HEIGHT, anchor='center', font='Gothic 40',
                               text="Type a single letter here, then press enter")

            print("There are no {}'s in the word".format(input_letter))
            # deduct a chance
            guesses_left -= 1

        # exit if correct guess
        if current_guess == secret_word:
            break


    print_exit_msg(current_guess, secret_word)


def get_word():
    """
    This function returns a secret word that the player is trying
    to guess in the game.  This function initially has a very small
    list of words that it can select from to make it easier for you
    to write and debug the main game playing program.  In Part II of
    writing this program, you will re-implement this function to
    select a word from a much larger list by reading a list of words
    from the file specified by the constant LEXICON_FILE.
    """
    f = open(LEXICON_FILE, "r")
    words = f.read().splitlines()
    return random.choice(words)

def update_word(current_guess, input_letter, ind_letter_in_word):
    '''
    Strings -> string
    inserts a certain letter in certain indexes in a word
    Input:  current_guess: how much of current word is guessed as displayed in status
            input_letter: inputted letter
            ind_letter_in_word: index where input letters can be found in secret word
    Output: (str) New current_guess with input_letter inserted in the right places
    '''
    tmp_list = list(current_guess)
    for i in ind_letter_in_word:
        tmp_list[i] = input_letter.upper()
    return ''.join(tmp_list)

def print_status(current_guess, guesses_left, canvas):
    '''
    string and integer -> string
    prints current status (how the guessed word looks, chances left) of the game
    '''
    # graphics eqt of print("The word now looks like this: " + current_guess)
    canvas.create_text(3/4 * CANVAS_WIDTH, CANVAS_HEIGHT/2, anchor='center', font='Gothic 100', text=current_guess)
    # graphics eqt of print("You have {} guesses left".format(guesses_left))
    canvas.create_text(CANVAS_WIDTH / 2, CANVAS_HEIGHT / 2 + 250, anchor='center', font='Gothic 100', text= "guesses left: " + str(guesses_left))


"""def get_input(canvas):
    input_msg = "Type a single letter here, then press enter"
    e1 = Entry(canvas)
    canvas.create_window(400, 10, window = e1)
    return e1
"""

def indexes(secret_word, input_letter):
    '''
    Strings -> enumerated integer(s)
    (when converted into a list) gives indexes of all locations where a certain letter appears in a word
    '''
    for i, x in enumerate(secret_word.lower()):
        if x == input_letter.lower():
            yield i

def print_exit_msg(current_guess, secret_word):
    '''
    Str -> str
    prints exit message based on final answer
    '''
    if current_guess == secret_word:
        print("Congratulations, the word is: {}".format(secret_word))
    else:
        print("Sorry, you lost. The secret word was: {}".format(secret_word))




def main():
    """
    To play the game, we first select the secret word for the
    player to guess and then play the game using that secret word.
    """
    # create a canvas
    canvas = make_canvas(CANVAS_WIDTH, CANVAS_HEIGHT, 'WordGuess')
    secret_word = get_word()
    play_game(secret_word, canvas)
    # canvas.mainloop()


######## DO NOT MODIFY ANY CODE BELOW THIS LINE ###########

# This function is provided to you and should not be modified.
# It creates a window that contains a drawing canvas that you
# will use to make your drawings.
def make_canvas(width, height, title=None):
    """
    DO NOT MODIFY
    Creates and returns a drawing canvas
    of the given int size with a blue border,
    ready for drawing.
    """
    objects = {}
    top = tkinter.Tk()
    top.minsize(width=width, height=height)
    if title:
        top.title(title)
    canvas = tkinter.Canvas(top, width=width + 1, height=height + 1)
    canvas.pack()
    """    # block screen resizing
    top.resizable(False, False)
    """
    #    canvas.bind("<Motion>", mouse_moved)
    return canvas


# This provided line is required at the end of a Python file
# to call the main() function.
if __name__ == "__main__":
    main()