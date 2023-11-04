import pygame

pygame.init()

WIDTH = 1200
HEIGHT = 1000

screen = pygame.display.set_mode([WIDTH, HEIGHT])
pygame.display.set_caption("Checkers (in-dev)")

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((10, 10, 10))

    # for obj in gameObjects:
    #     obj.update(screen)

    pygame.display.flip()


pygame.quit()