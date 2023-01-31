import random
import pygame
from math import *
import numpy as np

# Haven't researched anything, this is purely a guess
def lerp(p1, p2, t):
    # Calculate the delta's
    dy = p2[1] - p1[1]
    dx = p2[0] - p1[0]
    # Calculate the points
    tx = t * dx + p1[0]
    ty = t * dy + p1[1]
    return (tx, ty)

def toIntPixel(pixel):
    return (int(pixel[0]), int(pixel[1]))

def randomPos(maxX, maxY):
    return (random.randint(0, maxX), random.randint(0, maxY))

# Line
def line(line_1, line_2, precision):
    points = set()
    for t in np.arange(0, 1, precision):
        points.add(toIntPixel(lerp(line_1, line_2, t)))
    return points

# Quadratic Bezier Curve
def quadratic(line1_1, line1_2, line2_2, precision):
    points = set()
    for t in np.arange(0, 1, precision):
        line3_1 = lerp(line1_1, line1_2, t)
        line3_2 = lerp(line1_2, line2_2, t)
        points.add(toIntPixel(lerp(line3_1, line3_2, t)))
    return points

# Cubic Bezier Curve
def cubic(line1_1, line1_2, line2_1, line2_2, precision):
    points = set()
    line3_1 = line1_1
    line3_2 = line2_1
    for t in np.arange(0, 1, precision):
        line1_p = lerp(line1_1, line1_2, t)
        line2_p = lerp(line2_1, line2_2, t)
        line3_p = lerp(line3_1, line3_2, t)
        line4_p = lerp(line1_p, line2_p, t)
        line5_p = lerp(line2_p, line3_p, t)
        point = lerp(line4_p, line5_p, t)
        points.add(toIntPixel(point))
    return points

# Rendering
pygame.init()

WIDTH = 800
HEIGHT = 600

screen = pygame.display.set_mode([WIDTH, HEIGHT])
running = True

points = set()

precision = 0.0001

while running:
    screen.fill((55, 55, 77))

    line1_1 = randomPos(WIDTH, HEIGHT)
    line1_2 = randomPos(WIDTH, HEIGHT)
    line2_1 = randomPos(WIDTH, HEIGHT)
    line2_2 = randomPos(WIDTH, HEIGHT)

    # Did the user click the window close button?
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
            if event.key == pygame.K_0:
                points = set()
            if event.key == pygame.K_1:
                points.update(line(line1_1, line1_2, precision))
                points.update(line(line1_2, line2_2, precision))
            if event.key == pygame.K_2:
                points.update(quadratic(line1_1, line1_2, line2_2, precision))
            if event.key == pygame.K_3:
                points.update(cubic(line1_1, line1_2, line2_1, line2_2, precision))

    for pixel in points:
        screen.set_at(pixel, (222, 222, 222))
    
    pygame.display.flip()

pygame.quit()
quit()
