import pygame
import numpy

# pygame setup
pygame.init()
width, height = 1300, 700
screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()
running = True
dt = 0
randomOrientation = numpy.random.randint(0, 5, (height // 100, width // 100))

print(randomOrientation)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill("black")

    pygame.draw.rect(screen, "red", pygame.Rect(0, 0, 100, 100))
    pygame.draw.rect(screen, "green", pygame.Rect(width - 100, height - 100, 100, 100))

    for y in range(height // 100):
        for x in range(width // 100):
            x1CoordinateStart = (x + 1) * 100 - 100
            x2CoordinateStart = (x + 1) * 100 - 100
            x3CoordinateStart = (x + 1) * 100 - 100
            x4CoordinateStart = (x + 1) * 100

            y1CoordinateStart = (y + 1) * 100 - 100
            y2CoordinateStart = (y + 1) * 100
            y3CoordinateStart = (y + 1) * 100 - 100
            y4CoordinateStart = (y + 1) * 100 - 100

            x1CoordinateEnd = x1CoordinateStart + 100
            x2CoordinateEnd = x2CoordinateStart + 100
            x3CoordinateEnd = x3CoordinateStart
            x4CoordinateEnd = x4CoordinateStart

            y1CoordinateEnd = y1CoordinateStart
            y2CoordinateEnd = y2CoordinateStart
            y3CoordinateEnd = y3CoordinateStart + 100
            y4CoordinateEnd = y4CoordinateStart + 100

            if randomOrientation[y][x] == 0:
                pygame.draw.line(screen, "white", (x2CoordinateStart, y2CoordinateStart),
                                 (x2CoordinateEnd, y2CoordinateEnd))
                pygame.draw.line(screen, "white", (x3CoordinateStart, y3CoordinateStart),
                                 (x3CoordinateEnd, y3CoordinateEnd))
                pygame.draw.line(screen, "white", (x4CoordinateStart, y4CoordinateStart),
                                 (x4CoordinateEnd, y4CoordinateEnd))
            elif randomOrientation[y][x] == 1:
                pygame.draw.line(screen, "white", (x1CoordinateStart, y1CoordinateStart),
                                 (x1CoordinateEnd, y1CoordinateEnd))
                pygame.draw.line(screen, "white", (x3CoordinateStart, y3CoordinateStart),
                                 (x3CoordinateEnd, y3CoordinateEnd))
                pygame.draw.line(screen, "white", (x4CoordinateStart, y4CoordinateStart),
                                 (x4CoordinateEnd, y4CoordinateEnd))
            elif randomOrientation[y][x] == 2:
                pygame.draw.line(screen, "white", (x1CoordinateStart, y1CoordinateStart),
                                 (x1CoordinateEnd, y1CoordinateEnd))
                pygame.draw.line(screen, "white", (x2CoordinateStart, y2CoordinateStart),
                                 (x2CoordinateEnd, y2CoordinateEnd))
                pygame.draw.line(screen, "white", (x4CoordinateStart, y4CoordinateStart),
                                 (x4CoordinateEnd, y4CoordinateEnd))
            elif randomOrientation[y][x] == 3:
                pygame.draw.line(screen, "white", (x1CoordinateStart, y1CoordinateStart),
                                 (x1CoordinateEnd, y1CoordinateEnd))
                pygame.draw.line(screen, "white", (x2CoordinateStart, y2CoordinateStart),
                                 (x2CoordinateEnd, y2CoordinateEnd))
                pygame.draw.line(screen, "white", (x3CoordinateStart, y3CoordinateStart),
                                 (x3CoordinateEnd, y3CoordinateEnd))
            else:
                print(x, ", ", y)

    pygame.display.flip()
    dt = clock.tick(60) / 1000

pygame.quit()
