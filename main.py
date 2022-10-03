# Import library
import pygame

# initialize pygame
pygame.init()

# window size
screen_width = 500
screen_height = 300

# size variable
size = (screen_width, screen_height)

# Display the window
screen = pygame.display.set_mode(size)

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
