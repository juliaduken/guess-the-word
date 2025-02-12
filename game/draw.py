import pygame

import game.wordlist as wordlist
from game.config import BLUE, SCREEN_COLOR, WIDTH, HEIGHT, HOVER, ORANGE
from game.settings import FONT
from game.assets import home_image, win_image, lose_image
import game.states as states

def draw_background(screen):
    half_height = (HEIGHT // 2)
    screen.fill(SCREEN_COLOR, (0, 0, WIDTH, half_height))  # Upper half yellow
    screen.fill(BLUE, (0, half_height, WIDTH, half_height))  # Lower half blue

def draw_game_background(screen):
    height = 445
    screen.fill(SCREEN_COLOR, (0, 0, WIDTH, height))  # Upper half yellow
    screen.fill(BLUE, (0, height, WIDTH, height))  # Lower half blue

def draw_landing_page(screen):
    draw_background(screen)
    title_text = FONT.render("", True, HOVER)
    title_rect = title_text.get_rect(center=(WIDTH // 2, 150))
    screen.blit(title_text, title_rect)
    
    # Draw home image
    image_rect = home_image.get_rect(center=(WIDTH // 2, 350))
    screen.blit(home_image, image_rect)
    
    states.start_button.draw(screen)

def draw_game_screen(screen):
    draw_game_background(screen)
    # Draw user input grid
    y = 50
    for i in range(states.max_attempts):
        x = 100
        for j in range(len(wordlist.SECRET_WORD)):
            color = BLUE
            if i < len(states.attempt_colors):
                color = states.attempt_colors[i][j]
            pygame.draw.rect(screen, color, (x, y, 50, 50), border_radius=5)
            if i < len(states.attempts) and j < len(states.attempts[i]):
                text_surf = FONT.render(states.attempts[i][j], True, (64, 63, 59))
                screen.blit(text_surf, (x+15, y+10))
            elif i == len(states.attempts) and j < len(states.user_input):
                text_surf = FONT.render(states.user_input[j], True, (0, 0, 0))
                screen.blit(text_surf, (x+15, y+10))
            x += 60
        y += 60
    
    # Draw keyboard
    for button in states.key_buttons.values():
        button.draw(screen)

def draw_game_over_screen(screen):
    screen.fill(SCREEN_COLOR)
    if states.player_won:
        # Draw win image
        image_rect = win_image.get_rect(center=(WIDTH // 2, 350))
        screen.blit(win_image, image_rect)

    else:
        # Draw lose image
        image_rect = lose_image.get_rect(center=(WIDTH // 2, 350))
        screen.blit(lose_image, image_rect)

    message = f"The word was {wordlist.SECRET_WORD}."
    message_surf = FONT.render(message, True, ORANGE)
    message_rect = message_surf.get_rect(center=(WIDTH // 2, HEIGHT // 3.5))
    
    screen.blit(message_surf, message_rect)
    states.restart_button.draw(screen)

