# Import library
import pygame

# initialize pygame
pygame.init()

# Colors
background_color = (11, 19, 64)
player_color = (255, 255, 255)
ball_color = (80, 80, 80)
line_color = (80, 80, 80)


# Players size
players_width = 15
players_height = 90

# Player 1 coordinates
player_1_x = 50
player_1_y = 250

# Player 2 coordinates
player_2_x = 735
player_2_y = 250

# Ball coordinates
ball_x = 400
ball_y = 300
ball_radius = 20

# window size
screen_width = 800
screen_height = 600

# size variable
size = (screen_width, screen_height)

# Display the window
screen = pygame.display.set_mode(size)

# Title
pygame.display.set_caption("Pong Game")

# Icon
icon = pygame.image.load("icon.png")
pygame.display.set_icon(icon)

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
    # Fill the screen with color
    screen.fill(background_color)
    
    # Drawing area

    # Define the player 1 - left: rectangle
    player_1 = pygame.draw.rect(screen, player_color, (player_1_x, player_1_y, players_width, players_height))

    # Define the player 2 - right: rectangle
    player_2 = pygame.draw.rect(screen, player_color, (player_2_x, player_2_y, players_width, players_height))

    # Draw the ball
    ball = pygame.draw.circle(screen, ball_color,(ball_x, ball_y), ball_radius)

    # Draw the center line
    pygame.draw.line(screen, line_color,(screen_width/2,0),(screen_width/2, screen_height))


    # Update the window
    pygame.display.flip()