import os
import pygame
from game.config import ASSET_FOLDER, WHITE

# Load home, win, and lose images
try:
    home_path = os.path.join(ASSET_FOLDER, "home.png")
    home_image = pygame.image.load(home_path)
    home_image = pygame.transform.scale(home_image, (500, 350))
    
    win_path = os.path.join(ASSET_FOLDER, "win.png")
    win_image = pygame.image.load(win_path)
    win_image = pygame.transform.scale(win_image, (500, 350))

    lose_path = os.path.join(ASSET_FOLDER, "lose.png")
    lose_image = pygame.image.load(lose_path)
    lose_image = pygame.transform.scale(lose_image, (500, 350))

    # Create an oval mask
    mask = pygame.Surface((500, 350), pygame.SRCALPHA)
    pygame.draw.ellipse(mask, (255, 255, 255, 255), (0, 0, 500, 350))
    home_image.blit(mask, (0, 0), special_flags=pygame.BLEND_RGBA_MIN)

except pygame.error:
    home_image = pygame.Surface((500, 700))
    home_image.fill(WHITE)

    win_image = pygame.Surface((500, 700))
    win_image.fill(WHITE)
    
    lose_image = pygame.Surface((500, 700))
    lose_image.fill(WHITE)

# Load button images
try:
    start_button_path = os.path.join(ASSET_FOLDER, "start.png")
    start_button_image = pygame.image.load(start_button_path)
    start_button_image = pygame.transform.scale(start_button_image, (300, 150))

    back_button_path = os.path.join(ASSET_FOLDER, "back.png")
    back_button_image = pygame.image.load(back_button_path)
    back_button_image = pygame.transform.scale(back_button_image, (300, 150))

except pygame.error:
    start_button_image = None
    back_button_image = None