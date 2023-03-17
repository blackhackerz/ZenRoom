import pygame

def play_tic_tac_toe():
    pygame.init()
    # Set the window size
    window_size = (300, 300)
    # Create a new window
    screen = pygame.display.set_mode(window_size)
    # Set the window title
    pygame.display.set_caption("Tic Tac Toe")

    # Set the game background color
    background_color = (255, 255, 255)

    # Draw the game board
    screen.fill(background_color)
    pygame.draw.line(screen, (0, 0, 0), (100, 0), (100, 300), 5)
    pygame.draw.line(screen, (0, 0, 0), (200, 0), (200, 300), 5)
    pygame.draw.line(screen, (0, 0, 0), (0, 100), (300, 100), 5)
    pygame.draw.line(screen, (0, 0, 0), (0, 200), (300, 200), 5)

    # Game loop
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Update the display
        pygame.display.update()

    # Quit the game
    pygame.quit()

# Call the function to play Tic Tac Toe
play_tic_tac_toe()
