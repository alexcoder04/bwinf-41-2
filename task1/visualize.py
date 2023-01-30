#!/usr/bin/env python3

import time
import pygame

from lib import get_datapoints
from main12 import program

EXAMPLE = 6

pygame.init()

data = get_datapoints(EXAMPLE)
#print(data)
xs = [i[0] for i in data]
ys = [i[1] for i in data]

xmin = min(*xs)
ymin = min(*ys)

data = [(int(i[0] + abs(xmin)), int(i[1] + abs(ymin))) for i in data]
print(data)

xs = [i[0] for i in data]
ys = [i[1] for i in data]

xmax = max(*xs)
ymax = max(*ys)

print(xmax, ymax)

screen = pygame.display.set_mode([xmax*2, ymax*2])

route = [int(i.strip()) for i in input("route: ").split(",")]
#route = program(EXAMPLE, False)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill((0, 0, 0))
    for p in data:
        pygame.draw.rect(screen, (255, 255, 255), pygame.Rect(p[0] * 2 - 1, p[1] * 2 - 1, 3, 3))
    for i in range(len(route) - 1):
        pygame.draw.line(screen, (255, 0, 0), tuple([j*2 for j in data[route[i]]]), tuple([j*2 for j in data[route[i+1]]]))
    pygame.display.flip()
    time.sleep(0.1)

pygame.quit()
