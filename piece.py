import pygame

class Piece:
    def __init__(self, x, y, colour, board):
        self.x = x
        self.y = y
        self.colour = colour
        self.board = board
    
    def draw(self, screen):
        x = self.board.x
        y = self.board.y
        w = self.board.cellSize
        pygame.draw.circle(screen, self.colour, (x+w*self.x-w/2, y+w*self.y-w/2), w*2/5)
        pygame.draw.circle(screen, (200, 100, 200), (x+w*self.x-w/2, y+w*self.y-w/2), w*2/5, 4)