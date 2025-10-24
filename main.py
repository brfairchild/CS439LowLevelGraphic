import pygame
import math
import random

pygame.init()

width, height = 500, 500
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("CS439LowLevelGraphic")

background = (25, 5, 77)
triangleColors = [
    (255, 50, 50),
    (50, 255, 50),
    (50, 50, 255),
    (255, 255, 50),
    (255, 50, 255)
]

numTriangles = 5
triangleSize = 100
triangles = []

for i in range(numTriangles):
    points = [
        (0, -triangleSize),
        (-triangleSize * math.sin(math.pi / 3), triangleSize / 2),
        (triangleSize * math.sin(math.pi / 3), triangleSize / 2)
    ]
    speed = random.uniform(0.01, 0.05)
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
        rotatedPoints = [rotatePoint(x, y, i['angle']) for x, y in i['points']]
        screenPoints = [(int(x + width/2), int(y + height/2)) for x, y in rotatedPoints]
        
        # Draw triangle
        pygame.draw.line(screen, i['color'], screenPoints[0], screenPoints[1], 2)
        pygame.draw.line(screen, i['color'], screenPoints[1], screenPoints[2], 2)
        pygame.draw.line(screen, i['color'], screenPoints[2], screenPoints[0], 2)
        
        i['angle'] += i['speed']
    
    pygame.display.flip()
    clock.tick(60)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()