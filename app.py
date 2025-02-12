def main():
    # Import modules
    import pygame
    import sys

    # Import game modules
    import game.wordlist as wordlist
    from game.draw import draw_landing_page, draw_game_screen, draw_game_over_screen
    from game.config import SCREEN_COLOR, WIDTH, HEIGHT
    import game.states as states

    # Initialize pygame
    pygame.init()

    # Create window
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Guess the Word")

    # Main loop
    running = True
    while running:
        screen.fill(SCREEN_COLOR)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            # Handle mouse clicks
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                # Landing page clicks
                if states.game_state == states.LANDING:
                    states.start_button.check_click(pos)
                # Level select clicks
                elif states.game_state == states.LEVEL_SELECT:
                    for btn in states.level_buttons:
                        btn.check_click(pos)
                # Game over clicks
                elif states.game_state == states.GAME_OVER:
                    states.restart_button.check_click(pos)
                # Game clicks (keyboard input and color logic)
                elif states.game_state == states.GAME:
                    for letter, button in states.key_buttons.items():
                        if button.rect.collidepoint(pos):
                            if letter == "DELETE" and states.user_input:
                                states.user_input.pop()
                            elif letter == "ENTER" and len(states.user_input) == len(wordlist.SECRET_WORD):
                                if states.is_valid_word("".join(states.user_input)):
                                    states.attempts.append("".join(states.user_input))
                                    states.update_colors()
                                    states.check_win_or_lose()
                                states.user_input = []
                            elif letter not in ["DELETE", "ENTER"] and len(states.user_input) < len(wordlist.SECRET_WORD):
                                states.user_input.append(letter)
        
        # Handles drawing when game state changes
        if states.game_state == states.LANDING:
            draw_landing_page(screen)
        elif states.game_state == states.LEVEL_SELECT:
            for btn in states.level_buttons:
                btn.draw(screen)
        elif states.game_state == states.GAME:
            draw_game_screen(screen)
        elif states.game_state == states.GAME_OVER:
            states.restart_button.draw(screen)
            draw_game_over_screen(screen)
        
        pygame.display.flip()

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()