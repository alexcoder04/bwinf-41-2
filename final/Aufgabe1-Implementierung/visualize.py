#!/usr/bin/env python3

def normalize(data: list[tuple[float]]) -> list[tuple[int]]:
    """Normalize data for pygame coordinate system: only positive integers allowed"""
    xs = [i[0] for i in data]
    ys = [i[1] for i in data]

    xmin = min(*xs)
    ymin = min(*ys)

    # move all the points out of the negative space, add 1 pixel border
    return [(int(i[0] + abs(xmin) + 1), int(i[1] + abs(ymin) + 1)) for i in data]

def visualize(data: list[tuple[float]], route: list[int]):
    """Show points and the solution as a graphical pygame window"""

    # we import down here, so the modules get only loaded if the function is really called
    import time
    import pygame

    # prepare data
    data = normalize(data)

    xs = [i[0] for i in data]
    ys = [i[1] for i in data]

    # one pixels border each side
    xmax = max(*xs) + 2
    ymax = max(*ys) + 2

    # prepare window
    pygame.init()
    screen = pygame.display.set_mode([xmax*2, ymax*2])

    running = True
    while running:
        # quit event
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        # dark background
        screen.fill((5, 5, 5))
        # draw points in white
        for p in data:
            pygame.draw.rect(screen, (255, 255, 255), pygame.Rect(p[0] * 2 - 1, p[1] * 2 - 1, 3, 3))
        # draw route in red
        for i in range(len(route) - 1):
            pygame.draw.line(screen, (255, 0, 0), tuple([j*2 for j in data[route[i]]]), tuple([j*2 for j in data[route[i+1]]]))
        # update screen every 0.1 secs
        pygame.display.flip()
        time.sleep(0.1)

    pygame.quit()
