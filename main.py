import random
import sys

import pygame
from words import words

pygame.init()

WIDTH = 360
HEIGHT = 640
SQUARE_SIDE = 55

SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))

CORRECT_WORD = random.choice(words)

GUESSED_LETTER_FONT = pygame.font.Font("assets/Roboto-Bold.ttf", 50)
AVAILABLE_LETTER_FONT = pygame.font.Font("assets/Roboto-Regular.ttf", 25)

SCREEN.fill("white")
pygame.display.update()

colors = {
    "background": "#C9AE44",
    "letter_not_guessed": "#C94479",
    "letter_guessed": "#9444C9",
    "letter_place_guessed": "#79C944",

}

guesses_count = 0

guesses = [[]] * 6
current_guess = []
current_guess_string = ""
current_letter_bg_x = 90

indicators = []

game_result = ""


class Letter:
    def __init__(self, text, bg_position):
        # Initialises all the variables, including text, color, position, size, etc.
        pass

    def draw(self):
        # Puts the letter and text on the screen at the desired position
        pass

    def delete(self):
        # Fills the letter's square with default values, emptying it
        pass


class Indicator:
    def __init__(self, x, y, letter):
        pass

    def draw(self):
        # Puts indicator and text on the screen at the desired position
        pass


def check_guess(guess_to_check):
    pass


def play_again():
    pass


def reset():
    pass


def create_new_letter():
    pass


def delete_letter():
    pass


while True:
    if game_result != "":
        play_again()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
