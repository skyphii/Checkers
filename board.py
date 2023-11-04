import pygame
from piece import Piece

class Board:
    gridSize = 8

    def __init__(self):
        self.x = 100
        self.y = 0
        self.w = 1000
        self.h = 1000
        self.cellSize = self.w / Board.gridSize
        self.pieces = {}
    
    def draw(self, screen):
        alternate = False
        for y in range(Board.gridSize):
            for x in range(Board.gridSize):
                pygame.draw.rect(screen, (255, 255, 255) if alternate else (0, 0, 0), pygame.Rect(self.x+x*self.cellSize, self.y+y*self.cellSize, self.cellSize, self.cellSize))
                alternate = not alternate
            alternate = not alternate
        pygame.draw.rect(screen, (255, 255, 255), pygame.Rect(self.x, self.y, self.w, self.h), 2)
        for piece in self.pieces.values():
            piece.draw(screen)
    
    def addPiece(self, x, y, colour):
        self.pieces[(x, y)] = Piece(x, y, colour, self)

    def setup(self):
        self.addPiece(2, 1, (200, 0, 0))
        self.addPiece(4, 1, (200, 0, 0))
        self.addPiece(6, 1, (200, 0, 0))
        self.addPiece(8, 1, (200, 0, 0))
        self.addPiece(1, 2, (200, 0, 0))
        self.addPiece(3, 2, (200, 0, 0))
        self.addPiece(5, 2, (200, 0, 0))
        self.addPiece(7, 2, (200, 0, 0))
        self.addPiece(2, 3, (200, 0, 0))
        self.addPiece(4, 3, (200, 0, 0))
        self.addPiece(6, 3, (200, 0, 0))
        self.addPiece(8, 3, (200, 0, 0))

        self.addPiece(1, 6, (0, 0, 200))
        self.addPiece(3, 6, (0, 0, 200))
        self.addPiece(5, 6, (0, 0, 200))
        self.addPiece(7, 6, (0, 0, 200))
        self.addPiece(2, 7, (0, 0, 200))
        self.addPiece(4, 7, (0, 0, 200))
        self.addPiece(6, 7, (0, 0, 200))
        self.addPiece(8, 7, (0, 0, 200))
        self.addPiece(1, 8, (0, 0, 200))
        self.addPiece(3, 8, (0, 0, 200))
        self.addPiece(5, 8, (0, 0, 200))
        self.addPiece(7, 8, (0, 0, 200))
