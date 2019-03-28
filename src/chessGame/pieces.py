import pygame

b_pawn = pygame.image.load("../../img/black_pawn.png")
b_rook = pygame.image.load("../../img/black_rook.png")
b_knight = pygame.image.load("../../img/black_knight.png")
b_bishop = pygame.image.load("../../img/black_bishop.png")
b_queen = pygame.image.load("../../img/black_queen.png")
b_king = pygame.image.load("../../img/black_king.png")

w_pawn = pygame.image.load("../../img/white_pawn.png")
w_rook = pygame.image.load("../../img/white_rook.png")
w_knight = pygame.image.load("../../img/white_knight.png")
w_bishop = pygame.image.load("../../img/white_bishop.png")
w_queen = pygame.image.load("../../img/white_queen.png")
w_king = pygame.image.load("../../img/white_king.png")


b = [b_pawn, b_rook, b_knight, b_bishop, b_queen, b_king]
w = [w_pawn, w_rook, w_knight, w_bishop, w_queen, w_king]

b = [pygame.transform.scale(img, (80, 80)) for img in b]
w = [pygame.transform.scale(img, (80, 80)) for img in w]


class Piece:
    '''
    Every piece inherit from this class.
    '''
    img = -1

    def __init__(self, name, position, color):
        self.name = name
        self.position = position
        self.color = color
        self.selected = False

    def __repr__(self):
        return self.name

    def __str__(self):
        return self.name

    def draw(self, win):
        # draw piece on the screen
        if self.color == "white":
            drawThis = w[self.img]
        else:
            drawThis = b[self.img]

        x = self.position[1] + (self.position[1]*100) + 10
        y = self.position[0] + (self.position[0]*100) + 10

        if self.selected:
            pygame.draw.rect(win, (255, 0, 0), (x, y, 80, 80), 2)

        win.blit(drawThis, (x, y))


class Pawn(Piece):
    img = 0


class Rook(Piece):
    ig = 1


class Knight(Piece):
    img = 2


class Bishop(Piece):
    img = 3


class Queen(Piece):
    img = 4


class King(Piece):
    img = 5
