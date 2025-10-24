import pygame
import math
import random

# Initialize Pygame
pygame.init()

# Screen setup
width, height = 690, 720
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("CS439LowLevelGraphic")

background = (25, 5, 77)
triangleColors = [
    (255, 50, 50),
    (50, 255, 50),
    (50, 50, 255)
]


numTriangles = 1 
triangleSize = 150
triangles = []

# Basic triangle setup
for i in range(numTriangles):
    points = [
        (0, -triangleSize),
        (-triangleSize * math.sin(math.pi / 3), triangleSize / 2),
        (triangleSize * math.sin(math.pi / 3), triangleSize / 2)
    ]
    speed = 0.0  # Not spinning yet
    color = triangleColors[i % len(triangleColors)]
    triangles.append({'points': points, 'angle': 0, 'speed': speed, 'color': color})



def rotatePoint(x, y, angle):
    cosTheta = math.cos(angle)
    sinTheta = math.sin(angle)
    return x * cosTheta - y * sinTheta, x * sinTheta + y * cosTheta

###################### Main loop
running = True
clock = pygame.time.Clock()

while running:
    screen.fill(background)
    
    for i in triangles:
        screenPoints = [(int(x + width/2), int(y + height/2)) for x, y in i['points']]
        pygame.draw.line(screen, i['color'], screenPoints[0], screenPoints[1], 2)
        pygame.draw.line(screen, i['color'], screenPoints[1], screenPoints[2], 2)
        pygame.draw.line(screen, i['color'], screenPoints[2], screenPoints[0], 2)
    
    pygame.display.flip()
    clock.tick(60)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()
