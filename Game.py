import pygame
from random import random

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

pointx = 0
pointy = 0

ospeed = 100
osize = 10
oposx = 61
oposy = 81
odirectionx = 1
odirectiony = 1
oposx2 = 2000
oposy2 = 2000
odirectionx2 = 0
odirectiony2 = 0
oposx3 = 2000
oposy3 = 2000
odirectionx3 = 0
oposx4 = 2000
oposy4 = 2000
odirectiony4 = 0
ocolor = pygame.Color(60, 163, 23, 255)
ocolor2 = pygame.Color(47, 45, 59, 255)
ocolor3 = pygame.Color(47, 45, 59, 255)
ocolor4 = pygame.Color(47, 45, 59, 255)

key5 = True
key10 = True
key15 = True
key20 = True
pretres = False
key25 = True
tres = False
key30 = True
key35 = True
key40 = True
key45 = True
presecondo = False
key50 = True
secondo = False
key60 = True
key70 = True
prequad = False
key75 = True
quad = False
key80 = True
key90 = True
key100 = True

score = 0
changing = True

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

    pygame.draw.circle(screen, ocolor, (oposx, oposy), osize)
    oposx += odirectionx * ospeed * dt
    oposy += odirectiony * ospeed * dt

    pygame.draw.circle(screen, ocolor2, (oposx2, oposy2), osize)
    oposx2 += odirectionx2 * ospeed * dt
    oposy2 += odirectiony2 * ospeed * dt

    pygame.draw.circle(screen, ocolor3, (oposx3, oposy3), osize)
    oposx3 += odirectionx3 * ospeed * dt

    pygame.draw.circle(screen, ocolor4, (oposx4, oposy4), osize)
    oposy4 += odirectiony4 * ospeed * dt

    if oposx > 1239:
        odirectionx = -1
    if oposx < 61:
        odirectionx = 1
    if oposy > 689:
        odirectiony = -1
    if oposy < 81:
        odirectiony = 1


    if presecondo:
        if oposx2 > 1239:
            odirectionx2 = -1
        if oposx2 < 61:
            odirectionx2 = 1
        if oposy2 > 689:
            odirectiony2 = -1
        if oposy2 < 81:
            odirectiony2 = 1
    if pretres:
        if oposx3 > 1239:
            odirectionx3 = -1
        if oposx3 < 61:
            odirectionx3 = 1

    if prequad:
        if oposy4 > 689:
            odirectiony4 = -1
        if oposy4 < 81:
            odirectiony4 = 1

    if changing:
        pointx = 100 + (random() * 1100)
        pointy = 130 + (random() * 520)
        changing = False

    if pointx - 30 < player_pos.x < pointx + 30:
        if pointy - 30 < player_pos.y < pointy + 30:
            score += 1
            changing = True
    
    if oposx - osize < player_pos.x < oposx + osize:
        if oposy - osize < player_pos.y < oposy + osize:
            running = False

    if oposx2 - osize < player_pos.x < oposx2 + osize and secondo:
        if oposy2 - osize < player_pos.y < oposy2 + osize:
            running = False

    if oposx3 - osize < player_pos.x < oposx3 + osize and tres:
        if oposy3 - osize < player_pos.y < oposy3 + osize:
            running = False

    if oposx4 - osize < player_pos.x < oposx4 + osize and quad:
        if oposy4 - osize < player_pos.y < oposy4 + osize:
            running = False

    if score == 5 and key5:
        ospeed += 50
        key5 = False
    if score == 10 and key10:
        ocolor = pygame.Color(163, 163, 23)
        ospeed += 50
        osize += 5
        key10 = False
    if score == 15 and key15:
        ospeed += 50
        key15 = False
    if score == 20 and key20:
        ocolor = pygame.Color(163, 114, 23)
        ospeed += 50
        osize += 5
        oposx3 = 650
        oposy3 = 385
        odirectionx3 = 1
        pretres = True
        key20 = False
    if score == 25 and key25:
        tres = True
        ocolor3 = pygame.Color(163, 114, 23)
        key25 = False
    if score == 30 and key30:
        ocolor = pygame.Color(163, 39, 23)
        ospeed += 50
        osize += 5
        ocolor3 = pygame.Color(163, 39, 23)
        key30 = False
    if score == 35 and key35:
        ospeed += 50
        key35 = False
    if score == 40 and key40:
        ocolor = pygame.Color(159, 23, 163)
        ospeed += 50
        osize += 5
        ocolor3 = pygame.Color(159, 23, 163)
        key40 = False
    if score == 45 and key45:
        ospeed += 50
        odirectionx2 = -1
        odirectiony2 = -1
        oposy2 = 689 - oposy
        oposx2 = 1239 - oposx
        presecondo = True
        key45 = False
    if score == 50 and key50:
        ocolor = pygame.Color(51, 23, 163)
        secondo = True
        key50 = False
        ocolor2 = pygame.Color(51, 23, 163)
        ocolor3 = pygame.Color(51, 23, 163)
    if score == 60 and key60:
        ospeed += 100
        osize += 5
        key60 = False
    if score == 70 and key70:
        ospeed += 50
        osize += 5
        oposx4 = 650
        oposy4 = 385
        odirectiony4 = 1
        prequad = True
        key70 = False
    if score == 75 and key75:
        quad = True
        ocolor4 = pygame.Color(51, 23, 163)
        key75 = False
    if score == 80 and key80:
        ospeed += 100
        osize += 5
        key80 = False
    if score == 90 and key90:
        ospeed += 100
        osize += 5
        key90 = False
    if score == 100 and key100:
        ocolor = pygame.Color(31, 237, 230)
        ocolor2 = pygame.Color(31, 237, 230)
        ocolor3 = pygame.Color(31, 237, 230)
        ocolor4 = pygame.Color(31, 237, 230)
        ospeed += 100
        osize += 5
        key100 = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w] and player_pos.y > 85:
        player_pos.y -= 400 * dt
    if keys[pygame.K_s] and player_pos.y < 688:
        player_pos.y += 400 * dt
    if keys[pygame.K_a] and player_pos.x > 64:
        player_pos.x -= 400 * dt
    if keys[pygame.K_d] and player_pos.x < 1238:
        player_pos.x += 400 * dt
    if keys[pygame.K_SPACE] and boost > 0 and boost_timeout == False:
        boosting = True
        boost -= 4
        if keys[pygame.K_w] and player_pos.y > 85:
            player_pos.y -= 500 * dt
        if keys[pygame.K_s] and player_pos.y < 688:
            player_pos.y += 500 * dt
        if keys[pygame.K_a] and player_pos.x > 64:
            player_pos.x -= 500 * dt
        if keys[pygame.K_d] and player_pos.x < 1238:
            player_pos.x += 500 * dt 

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