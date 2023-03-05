# -*- coding: utf-8 -*-
"""
Created on Mon Mar  6 01:13:32 2023

@author: Nicholas
"""

import pygame, sys, time
from pygame.locals import *

# User-defined classes

# User-defined functions

def main():
# Initialize pygame
    pygame.init()
    pygame.key.set_repeat(20, 20)

# Set window size and title, and frame delay
    surfaceSize = (500, 400)
    ​windowTitle = ​'Pong'
    ​frameDelay =​ ​0.01​ ​# smaller is faster game

​# Create the window

    surface =
    pygame.display.set_mode(surfaceSize, 0, 0)
    pygame.display.set_caption(windowTitle)

# create and initialize objects
    gameOver = False
    ​fgColor = pygame.Color('white')
    bgColor = pygame.Color('black')
    center = [surfaceSize[0] // 2,
              surfaceSize[1] // 2]
    radius = 5
    speed = [4, 1]
    pWidth = 10
    pHeight = 40
    pXOffset = 100
    pYOffset = (surfaceSize[1] - pHeight) // 2
    pLeft = pygame.Rect(pXOffset, pYOffset,
                        pWidth, pHeight)
    pRight = pygame.Rect(surfaceSize[0] -
                         pXOffset - pWidth, pYOffset, pWidth, pHeight)
    pMove = 10
    score = [0,0]

​# Draw objects

    ​pygame.draw.circle(surface,​ fgColor, ​center,
                        radius​)
    pygame.draw.rect(surface, fgColor, pLeft)
    pygame.draw.rect(surface, fgColor, pRight)

​# Refresh the display
    pygame.display.update()

# Loop forever
while True:
# Handle events
for event in pygame.event.get():
    if event.type == QUIT:
        pygame.quit()
        sys.exit()
        # Handle additional events
    if event.type == KEYDOWN and not
        gameOver:
            handleKeyDown(event, pLeft, pRight,
                          pMove, surface)

# Update and draw objects for next frame
    gameOver = update(​fgColor, bgColor,
                      center,​ ​radius, speed, pLeft, pRight,​ ​score,
                      surface)

# Refresh the display
    pygame.display.update()

# Set the frame speed by pausing between
    frames
    time.sleep(frameDelay)

def update(​fgColor, bgColor,​ ​center,​ ​radius,
           speed, pLeft, pRight,​ ​score,​ ​surface)​:


    ​maxScore = 11
    ​if ​score[0] >= maxScore or score[1] >=
        maxScore​ :
            ​drawScore(score, fgColor, bgColor,
                       surface)
            return True
        else:
            surface.fill(bgColor)
            moveBall(center, radius, speed, pLeft,
                     pRight, surface)
            pygame.draw.circle(surface, fgColor,
                               center, radius)
            pygame.draw.rect(surface, fgColor, pLeft)

            pygame.draw.rect(surface, fgColor,
                             pRight)
            ​drawScore(score, fgColor, bgColor,
                       surface)
            return False

def moveBall(center, radius, speed, pLeft,
             pRight, score, surface):

    size = surface.get_size()
    for coord in range(0, 2):
        # move ball
        center[coord] = center[coord] +
        speed[coord]
        # check left or top collisions
        if center[coord] < radius:
            speed[coord] = - speed[coord]
        if coord == 0:
                score[1] = score[1] + 1
                # check right or bottom collisions
        if center[coord] + radius > size[coord]:
                    speed[coord] = - speed[coord]
        if coord == 0:
            score[0] = score[0] + 1
                        # check paddle collisions
        if pRight.collidepoint(center) and speed[0]
                            > 0 :
                                speed[0] = -speed[0]

        if pLeft.collidepoint(center) and speed[0] <
            0 :
                speed[0] = -speed[0]

def drawScore(score, fgColor, bgColor,
surface):
# Draw the score at the top of the surface.
# - score is a list that contains the int
left player's score
# and the int right player's score
# - fgColor is the pygame.Color of the ball
and paddles
# - bgColor is the background color used to
erase
# - surface is the window's pygame.Surface
object

fontSize = 72
surfaceWidth = surface.get_width()
font = pygame.font.SysFont(None, fontSize,
True)
textSurface = font.render(str(score[0]),
True, fgColor, bgColor)
surface.blit(textSurface, (0,0))
textSurface = font.render(str(score[1]),
True, fgColor, bgColor)

textWidth = textSurface.get_width()
surface.blit(textSurface, (surfaceWidth -
textWidth,0))

def paddleUp(paddle, delta, surface) :
# Move the paddle up, but not outside the
surface
# - paddle is a pygame.Rect that represents
a player's paddle
# - delta is an int number of pixels to move
the paddle
# - bgColor is the background color used to
erase
# - surface is the window's pygame.Surface
object

if paddle.top < delta :
delta = paddle.top
paddle.move_ip(0, -delta)

def paddleDown(paddle, delta, surface) :
# Move the paddle down, but not outside the
surface
# - paddle is a pygame.Rect that represents
a player's paddle

# - delta is an int number of pixels to move
the paddle
# - bgColor is the background color used to
erase
# - surface is the window's pygame.Surface
object

maxBottom = surface.get_height()
if maxBottom - paddle.bottom < delta :
delta = maxBottom - paddle.bottom
paddle.move_ip(0, delta)

def handleKeyDown(event, pLeft, pRight, pDelta,
surface):
# Respond to the player pressing a key by
moving one of
# the paddles if the key was appropriate.
# - pLeft is a pygame.Rect that represents
the left player's paddle
# - pRight is a pygame.Rect that represents
the right player's paddle
# - pDelta is the int number of pixels to
move a paddle
# - surface is the window's pygame.Surface
object

if event.key == K_q : # left paddle up
paddleUp(pLeft, pDelta, surface)
if event.key == K_a : # left paddle down
paddleDown(pLeft, pDelta, surface)
if event.key == K_p : # right paddle up
paddleUp(pRight, pDelta, surface)
if event.key == K_l : # right paddle down
paddleDown(pRight, pDelta, surface)

main()