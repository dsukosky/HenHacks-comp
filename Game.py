import pygame
import random

pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
dt = 0

player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)

boost = 100
boosting = False
boost_timeout = False
boost_color = "white"

pointx = 70
pointy = 200

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    if boost_timeout:
        boost_color = "red"
    else:
        boost_color = "white"
    boosting = False

    # backround
    screen.fill("black")

    # player controls
    pygame.draw.circle(screen, "white", player_pos, 10)
    pygame.draw.line(screen, boost_color, (1150, 50), (1150 + boost, 50), 10)
    
    pygame.draw.line(screen, "white", (50, 70), (1250, 70), 1)
    pygame.draw.line(screen, "white", (50, 700), (1250 ,700), 1)
    pygame.draw.line(screen, "white", (50, 70), (50, 700), 1)
    pygame.draw.line(screen, "white", (1250, 70), (1250, 700), 1)

    pygame.draw.circle(screen, "yellow", (pointx, pointy), 5)

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w] and player_pos.y > 85:
        player_pos.y -= 300 * dt
    if keys[pygame.K_s] and player_pos.y < 688:
        player_pos.y += 300 * dt
    if keys[pygame.K_a] and player_pos.x > 64:
        player_pos.x -= 300 * dt
    if keys[pygame.K_d] and player_pos.x < 1238:
        player_pos.x += 300 * dt
    if keys[pygame.K_SPACE] and boost > 0 and boost_timeout == False:
        boosting = True
        boost -= 1
        if keys[pygame.K_w] and player_pos.y > 85:
            player_pos.y -= 600 * dt
        if keys[pygame.K_s] and player_pos.y < 688:
            player_pos.y += 600 * dt
        if keys[pygame.K_a] and player_pos.x > 64:
            player_pos.x -= 600 * dt
        if keys[pygame.K_d] and player_pos.x < 1238:
            player_pos.x += 600 * dt 

    if not boosting and boost < 100:
        boost += 1
    if boost == 0:
        boost_timeout = True
    if boost > 99:
        boost_timeout = False

    # flip() the display to put your work on screen
    pygame.display.flip()

    dt = clock.tick(60) / 1000 # limits FPS to 60

pygame.quit()