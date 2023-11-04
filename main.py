import pygame
from utils import Utils
from board import Board

pygame.init()

screen = pygame.display.set_mode([Utils.WIDTH, Utils.HEIGHT])
pygame.display.set_caption("Checkers (in-dev)")

gameObjects = []
board = Board()
gameObjects.append(board)
board.setup()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((40, 10, 40))

    for obj in gameObjects:
        obj.draw(screen)

    pygame.display.flip()


pygame.quit()