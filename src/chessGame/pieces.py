import pygame


class Piece:
    '''
    Every piece inherit from this class.
    '''

    def __init__(self, name, position, color):
        self.name = name
        self.position = position
        self.color = color
        self.selected = False
        self.move_list = []

    def __repr__(self):
        return self.name

    def __str__(self):
        return self.name

    def draw(self, win):
        '''
        Draws pieces on the board.
        '''
        x = self.position[1] + (self.position[1]*100) + 5
        y = self.position[0] + (self.position[0]*100) + 5

        if self.selected:
            pygame.draw.rect(win, (255, 0, 0), (x, y, 80, 80), 2)

        win.blit(self.image, (x, y))

    def draw_moves(self, win, board):
        '''
        Draws all possible moves of selected piece
        '''
        for position in self.available_moves(board):
            x = position[0] + (position[0]*100) + 45
            y = position[1] + (position[1]*100) + 45
            # print(x, y)
            pygame.draw.circle(win, (255, 0, 0), (x, y), 20, 20)


class Pawn(Piece):
    def __init__(self, name, position, color):
        super().__init__(name, position, color)
        if color == "white":
            self.image = pygame.transform.scale(
                pygame.image.load("../../img/white_pawn.png"), (80, 80))
        else:
            self.image = pygame.transform.scale(
                pygame.image.load("../../img/black_pawn.png"), (80, 80))
        self.first_move = True

    def available_moves(self, board):
        moves = []
        # i - row
        # j - col
        i, j = self.position
        if self.color == "white":
            if i < 7:
                if board[i-1][j] == 0:
                    moves.append((j, i - 1))
                    if self.first_move and board[i - 2][j] == 0:
                        moves.append((j, i - 2))

                if j < 7:
                    if board[i - 1][j + 1] != 0 and board[i - 1][j + 1].color != self.color:
                        moves.append((j + 1, i - 1))

                if j > 0:
                    if board[i - 1][j - 1] != 0 and board[i - 1][j - 1].color != self.color:
                        moves.append((j - 1, i - 1))
        else:
            if i > 0:
                if board[i+1][j] == 0:
                    moves.append((j, i + 1))
                    if self.first_move and board[i + 2][j] == 0:
                        moves.append((j, i + 2))

                if j < 7:
                    if board[i + 1][j + 1] != 0 and board[i + 1][j + 1].color != self.color:
                        moves.append((j + 1, i + 1))

                if j > 0:
                    if board[i + 1][j - 1] != 0 and board[i + 1][j - 1].color != self.color:
                        moves.append((j - 1, i + 1))

        return moves


class Rook(Piece):
    def __init__(self, name, position, color):
        super().__init__(name, position, color)
        if color == "white":
            self.image = pygame.transform.scale(
                pygame.image.load("../../img/white_rook.png"), (80, 80))
        else:
            self.image = pygame.transform.scale(
                pygame.image.load("../../img/black_rook.png"), (80, 80))

    def available_moves(self, board):
        moves = []
        i, j = self.position
        # forward
        if i < 7:
            for new_pos in range(i - 1, -1, -1):
                if board[new_pos][j] != 0 and board[new_pos][j].color != self.color:
                    moves.append((j, new_pos))
                    break
                moves.append((j, new_pos))
         # left
        if j < 7:
            for new_pos in range(j - 1, -1, -1):
                if board[i][new_pos] != 0 and board[i][new_pos].color != self.color:
                    moves.append((new_pos, i))
                    break
                moves.append((new_pos, i))
         # backward
        if i > 0:
            for new_pos in range(i + 1, 8):
                if board[new_pos][j] != 0 and board[new_pos][j].color != self.color:
                    moves.append((j, new_pos))
                    break
                moves.append((j, new_pos))
         # right
        if j > 0:
            for new_pos in range(j + 1, 8):
                if board[i][new_pos] != 0 and board[i][new_pos].color != self.color:
                    moves.append((new_pos, i))
                    break
                moves.append((new_pos, i))

        return moves


class Knight(Piece):
    def __init__(self, name, position, color):
        super().__init__(name, position, color)
        if color == "white":
            self.image = pygame.transform.scale(
                pygame.image.load("../../img/white_knight.png"), (80, 80))
        else:
            self.image = pygame.transform.scale(
                pygame.image.load("../../img/black_knight.png"), (80, 80))

    def available_moves(self, board):
        moves = []
        i, j = self.position
        if i > 0:
            if j > 0:
                if board[i - 2][j - 1] == 0 or board[i - 2][j - 1].color != self.color:
                    moves.append((j - 1, i - 2))

                if board[i - 1][j - 2] == 0 or board[i - 1][j - 2].color != self.color:
                    moves.append((j - 2, i - 1))

            if j < 7:
                if board[i - 2][j + 1] == 0 or board[i - 2][j - 1].color != self.color:
                    moves.append((j + 1, i - 2))

                if board[i - 1][j + 2] == 0 or board[i - 1][j - 2].color != self.color:
                    moves.append((j + 2, i - 1))

        return moves


class Bishop(Piece):
    def __init__(self, name, position, color):

        super().__init__(name, position, color)
        if color == "white":
            self.image = pygame.transform.scale(
                pygame.image.load("../../img/white_bishop.png"), (80, 80))
        else:
            self.image = pygame.transform.scale(
                pygame.image.load("../../img/black_bishop.png"), (80, 80))


class Queen(Piece):
    def __init__(self, name, position, color):
        super().__init__(name, position, color)
        if color == "white":
            self.image = pygame.transform.scale(
                pygame.image.load("../../img/white_queen.png"), (80, 80))
        else:
            self.image = pygame.transform.scale(
                pygame.image.load("../../img/black_queen.png"), (80, 80))


class King(Piece):
    def __init__(self, name, position, color):
        super().__init__(name, position, color)
        if color == "white":
            self.image = pygame.transform.scale(
                pygame.image.load("../../img/white_king.png"), (80, 80))
        else:
            self.image = pygame.transform.scale(
                pygame.image.load("../../img/black_king.png"), (80, 80))
