import random
import sys

import pygame
from words import words

pygame.init()

WIDTH = 360
HEIGHT = 640
SQUARE_SIDE = 56

LETTER_X_SPACING = 50
LETTER_Y_SPACING = 12
LETTER_SIZE = 40

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
current_letter_bg_x = 50

indicators = []

game_result = ""


class Letter:
    def __init__(self, text, bg_position):
        # Initialises all the variables, including text, color, position, size, etc.
        self.bg_color = "white"
        self.text_color = "black"
        self.bg_position = bg_position
        self.bg_x = bg_position[0]
        self.bg_y = bg_position[1]
        self.bg_rect = (bg_position[0], self.bg_y, LETTER_SIZE, LETTER_SIZE)
        self.text = text
        self.text_position = (self.bg_x+20, self.bg_position[1]+18)
        self.text_surface = GUESSED_LETTER_FONT.render(self.text, True, self.text_color)
        self.text_rect = self.text_surface.get_rect(self.text_position)


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
    global current_guess_string, current_letter_bg_x
    current_guess_string += key_pressed
    new_letter = Letter(key_pressed, (current_letter_bg_x, guesses_count*56 + LETTER_Y_SPACING))
    current_letter_bg_x += LETTER_X_SPACING
    guesses[guesses_count].append(new_letter)
    current_guess.append(new_letter)
    for guess in guesses:
        for letter in guess:
            letter.draw()


def delete_letter():
    global current_guess_string, current_letter_bg_x
    guesses[guesses_count][-1].delete()
    guesses[guesses_count].pop()
    current_guess_string = current_guess_string[:-1]
    current_guess.pop()
    current_letter_bg_x -= LETTER_X_SPACING


while True:
    if game_result != "":
        play_again()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                if game_result != "":
                    reset()
                else:
                    if len(current_guess_string) == 5 and current_guess_string.lower() in words:
                        check_guess(current_guess)

            elif event.key == pygame.K_BACKSPACE:
                if len(current_guess_string) > 0:
                    delete_letter()
            else:
                key_pressed = event.unicode.upper()
                if key_pressed in "QWERTYUIOPASDFGHJKLZXCVBNM" and key_pressed != "":
                    if len(current_guess_string) < 5:
                        create_new_letter()

