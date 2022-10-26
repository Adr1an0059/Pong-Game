# Import libraries
import pygame
import random as rd
from pygame import mixer as mx

# initialize pygame
pygame.init()

# Colors
background_color = (11, 19, 64)
player_color = (255, 255, 255)
ball_color = (80, 80, 80)
line_color = (255, 255, 255)

# Background music
mx.music.load("music.wav")
mx.music.play(-1)

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

ball_speed_x = 0.5
ball_speed_y = 0.5

# window size
screen_width = 800
screen_height = 600

# size variable
size = (screen_width, screen_height)

# Display the window
screen = pygame.display.set_mode(size)

# Title
pygame.display.set_caption("Pong Game")

# Score variables
player_1_score = 0
player_2_score = 0

# Score font
score_font = pygame.font.Font("Font.ttf", 32)

# Win font
win_font = pygame.font.Font("Font.ttf", 64)


# Score position in the screen (player 1)
player_1_score_x = 10
player_1_score_y = 10

# Score position in the screen (player 2)
player_2_score_x = screen_width - 165
player_2_score_y = 10

# Win text position
win_x = 260
win_y = 220
win_x_2 = 260
win_y_2 = 360

# Player 1 score function
def show_score_1(x, y):
    score_1 = score_font.render("Player one: " + str (player_1_score), True, (0, 0, 0))
    screen.blit(score_1, (x, y))

def show_score_2(x, y):
    score_2 = score_font.render("Player two: " + str (player_2_score), True, (0, 0, 0))
    screen.blit(score_2, (x, y))

# Beta (Play Again)

#def play_again(x, y):
#    text_again = score_font.render("¿Press Space to play again") + str (player_1_score), True, (0, 0, 0)
#    screen.blit(text_again, (x, y))
    
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
                player_1_y_speed = -0.9

            if event.key == pygame.K_s:
                player_1_y_speed = 0.9
            
            # Player 2
            if event.key == pygame.K_UP:
                player_2_y_speed = -0.9

            if event.key == pygame.K_DOWN:
                player_2_y_speed = 0.9

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

        lose_sound = mx.Sound("lose.wav")
        lose_sound.play()
        player_1_score += 1

        ball_x = screen_width/2
        ball_y = screen_height/2
        ball_speed_x *= rd.choice([-1, 1])

    elif ball_x < 0:
        lose_sound.play()
        player_2_score += 1

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

    # Draw the center line
    pygame.draw.line(screen, line_color,(screen_width/2,0),(screen_width/2, screen_height))

    # Draw the ball
    ball = pygame.draw.circle(screen, ball_color,(ball_x, ball_y), ball_radius)

    # Player win
    if player_1_score >= 5:
        player_1_y_speed = 0
        player_2_y_speed = 0
        ball_y = 2000
        ball_speed_x = 0
        ball_speed_y = 0
        player_y = 0
        win_text = win_font.render("PLAYER 1 WIN", True, (17, 7, 131))
        screen.blit(win_text, (win_x, win_y))

    
    elif player_2_score >= 5:
        player_1_y_speed = 0
        player_2_y_speed = 0
        ball_y = 2000
        ball_speed_x = 0
        ball_speed_y = 0
        player_y = 0
        win_text = win_font.render("PLAYER 2 WIN", True, (17, 7, 131))
        screen.blit(win_text, (win_x_2, win_y_2))

    # Drawing area

    # Define the player 1 - left: rectangle
    player_1 = pygame.draw.rect(screen, player_color, (player_1_x, player_1_y, players_width, players_height))

    # Define the player 2 - right: rectangle
    player_2 = pygame.draw.rect(screen, player_color, (player_2_x, player_2_y, players_width, players_height))

    # Colitions
    if ball.colliderect(player_1) or ball.colliderect(player_2):
        ball_speed_x *= -1
        ball_sound = mx.Sound("smash.wav")
        ball_sound.play()

    # Call the show score_1 function
    show_score_1(player_1_score_x, player_1_score_y)

    # Call the show score_2 function
    show_score_2(player_2_score_x, player_2_score_y)


    # Update the window
    pygame.display.flip()