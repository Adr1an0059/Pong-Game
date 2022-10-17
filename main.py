# Import library
import pygame
import random as rd

# initialize pygame
pygame.init()

# Colors
background_color = (11, 19, 64)
player_color = (255, 255, 255)
ball_color = (80, 80, 80)
line_color = (255, 255, 255)

# Players size
players_width = 15
players_height = 90

# Player 1 coordinates
player_1_x = 50
player_1_y = 300 - (players_height/2)
player_1_y_speed = 0

# Player 2 coordinates
player_2_x = 750 - (players_width)
player_2_y = player_1_y
player_2_y_speed = 0

# Ball coordinates
ball_x = 400
ball_y = 300
ball_radius = 20

ball_speed_x = 0.4
ball_speed_y = 0.4

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

        # Player key controls

        # Checks for KEYDOWN event
        if event.type == pygame.KEYDOWN:
            
            # Player 1
            if event.key == pygame.K_w:
                player_1_y_speed = -0.7

            if event.key == pygame.K_s:
                player_1_y_speed = 0.7
            
            # Player 2
            if event.key == pygame.K_UP:
                player_2_y_speed = -0.7

            if event.key == pygame.K_DOWN:
                player_2_y_speed = 0.7

        # Checks for KEYUP event
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_DOWN or event.key == pygame.K_UP:
                player_2_y_speed = 0

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_w or event.key == pygame.K_s:
                player_1_y_speed = 0

    # Players movement
    player_1_y += player_1_y_speed
    player_2_y += player_2_y_speed

    # Ball movement
    ball_x += ball_speed_x
    ball_y += ball_speed_y

    # Ball boundaries: top or buttom
    if ball_y >(screen_height - ball_radius) or ball_y < ball_radius:
        ball_speed_y *= -1
    
    # Ball boundaries (right or left) and score update
    if ball_x > screen_width:
        ball_x = screen_width/2
        ball_y = screen_height/2
        ball_speed_x *= rd.choice([-1, 1])

    elif ball_x < 0:
        ball_x = screen_width/2
        ball_y = screen_height/2
        ball_speed_x *= rd.choice([-1, 1])

    # Player y boundaries, Up and Down

    # Player 1
    if player_1_y <= 0:
        player_1_y = 0   

    if player_1_y >= screen_height - players_height:
        player_1_y = screen_height - players_height

    # Player 2
    if player_2_y <= 0:
        player_2_y = 0   

    if player_2_y >= screen_height - players_height:
        player_2_y = screen_height - players_height

    # Fill the screen with color
    screen.fill(background_color)
    
    # Drawing area

    # Define the player 1 - left: rectangle
    player_1 = pygame.draw.rect(screen, player_color, (player_1_x, player_1_y, players_width, players_height))

    # Define the player 2 - right: rectangle
    player_2 = pygame.draw.rect(screen, player_color, (player_2_x, player_2_y, players_width, players_height))

    # Draw the center line
    pygame.draw.line(screen, line_color,(screen_width/2,0),(screen_width/2, screen_height))

    # Draw the ball
    ball = pygame.draw.circle(screen, ball_color,(ball_x, ball_y), ball_radius)

    # Update the window
    pygame.display.flip()