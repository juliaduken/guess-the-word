import random
from game.config import WIDTH, BLUE, WHITE, GREEN, GRAY, HOVER, YELLOW
import game.wordlist as wordlist
from game.ui import Button
from game.assets import start_button_image, back_button_image

# Game constants
user_input = []
max_attempts = 6 # Default value
player_won = False
attempt_colors = []
attempts = []

# Game States
LANDING, LEVEL_SELECT, GAME, GAME_OVER = "landing", "level_select", "game", "game_over"
game_state = LANDING

# Functions to change game state
def go_to_level_select():
    global game_state
    game_state = LEVEL_SELECT

def go_to_game(difficulty):
    global game_state, max_attempts
    game_state = GAME
    max_attempts = difficulty
    
def go_to_game_over(win):
    global game_state, player_won
    game_state = GAME_OVER
    player_won = win

def go_to_landing():
    global game_state, attempts, user_input, attempt_colors, letter_colors, attempt_colors, SECRET_WORD
    game_state = LANDING
    # Reset game variables
    attempts = []
    user_input = []
    attempt_colors = []
    letter_colors = {letter: WHITE for letter in "QWERTYUIOPASDFGHJKLZXCVBNM"}
    setup_keyboard()
    wordlist.SECRET_WORD = random.choice(wordlist.WORD_LIST).upper()


def check_win_or_lose():
    global attempts, max_attempts
    if attempts and attempts[-1] == wordlist.SECRET_WORD:
        go_to_game_over(True)
        return
    if len(attempts) >= max_attempts:
        go_to_game_over(False)

# Function to validate if the entered word is in the word list
def is_valid_word(word):
    return word in wordlist.WORD_LIST


# Keyboard Setup
keyboard_layout = [
    "QWERTYUIOP",
    "ASDFGHJKL",
    "ZXCVBNM"
]

key_buttons = {}
letter_colors = {letter: WHITE for letter in "QWERTYUIOPASDFGHJKLZXCVBNM"}

def setup_keyboard():
    start_x = 50
    start_y = 470
    key_width = 40
    key_height = 50
    padding = 10
    
    y = start_y
    for row in keyboard_layout:
        x = (WIDTH - (len(row) * (key_width + padding) - padding)) // 2
        for letter in row:
            key_buttons[letter] = Button(letter, x, y, key_width, key_height, letter_colors[letter], HOVER)
            x += key_width + padding
        y += key_height + padding - 3
    
    key_buttons["DELETE"] = Button("DEL", WIDTH - 150, y, 70, key_height, GRAY, HOVER)
    key_buttons["ENTER"] = Button("ENTER", 50, y, 100, key_height, GREEN, HOVER)

setup_keyboard()

def update_colors():
    global letter_colors, attempt_colors
    word_colors = []
    for i, letter in enumerate(attempts[-1]):
        if wordlist.SECRET_WORD[i] == letter:
            letter_colors[letter] = GREEN
            word_colors.append(GREEN)
        elif letter in wordlist.SECRET_WORD and letter_colors[letter] != GREEN:
            letter_colors[letter] = YELLOW
            word_colors.append(YELLOW)
        else:
            if letter_colors[letter] == WHITE:
                letter_colors[letter] = GRAY
            word_colors.append(GRAY)
    attempt_colors.append(word_colors)
    setup_keyboard()

# Buttons
start_button = Button("Start Game", 100, 550, 300, 150, YELLOW, HOVER, go_to_level_select, image=start_button_image)
level_buttons = [
    Button("Easy", 170, 200, 160, 50, BLUE, HOVER, lambda: go_to_game(6)),
    Button("Medium", 170, 270, 160, 50, BLUE, HOVER, lambda: go_to_game(4)),
    Button("Hard", 170, 340, 160, 50, BLUE, HOVER, lambda: go_to_game(3))
]
restart_button = Button("Back", 100, 550, 300, 150, YELLOW, HOVER, go_to_landing, image=back_button_image)
