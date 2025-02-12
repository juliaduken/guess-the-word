from game.settings import BUTTON_FONT

import pygame

class Button:
    def __init__(self, text, x, y, width, height, color, hover_color, action=None, image=None):
        self.text = text
        self.rect = pygame.Rect(x, y, width, height)
        self.color = color
        self.hover_color = hover_color
        self.action = action
        self.image = image

    def draw(self, screen):
        mouse_pos = pygame.mouse.get_pos()
        current_color = self.hover_color if self.rect.collidepoint(mouse_pos) else self.color
        
        if self.image:
            screen.blit(self.image, self.rect.topleft)
        else:
            pygame.draw.rect(screen, current_color, self.rect, border_radius=15)
            text_surf = BUTTON_FONT.render(self.text, True, (64, 63, 59))
            text_rect = text_surf.get_rect(center=self.rect.center)
            screen.blit(text_surf, text_rect)
    
    def check_click(self, pos):
        if self.rect.collidepoint(pos) and self.action:
            return self.action()

