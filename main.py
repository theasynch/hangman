"""
Main program file for the game.
"""


import random
from words import word_list

def get_word():
    word = random.choice(word_list)
    return word.upper()