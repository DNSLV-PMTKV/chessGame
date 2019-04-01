from pieces import *


class Board:
    def __init__(self):
        # initialize board as 2d array of 0's
        self.board = [[0 for x in range(8)] for y in range(8)]

        # black pawns
        for i in range(8):
            self.board[1][i] = Pawn("BlackPawn{}".format(i+1), (1, i), "black")

        # black pieces
        self.board[0][0] = Rook("BlackRookLeft", (0, 0), "black")
        self.board[0][1] = Knight("BlackKnightLeft", (0, 1), "black")
        self.board[0][2] = Bishop("BlackBishopLeft", (0, 2), "black")
        self.board[0][3] = Queen("BlackQueen", (0, 3), "black")
        self.board[0][4] = King("BlackKing", (0, 4), "black")
        self.board[0][5] = Bishop("BlackBishopRight", (0, 5), "black")
        self.board[0][6] = Knight("BlackKnightRight", (0, 6), "black")
        self.board[0][7] = Rook("BlackRookRight", (0, 7), "black")

        # white pawns
        for i in range(8):
            self.board[6][i] = Pawn("WhitePawn{}".format(i+1), (6, i), "white")

        # white pieces
        self.board[7][0] = Rook("WhiteRookLeft", (7, 0), "white")
        self.board[7][1] = Knight("WhiteKnightLeft", (7, 1), "white")
        self.board[7][2] = Bishop("WhiteBishopLeft", (7, 2), "white")
        self.board[7][3] = Queen("WhiteQueen", (7, 3), "white")
        self.board[7][4] = King("WhiteKing", (7, 4), "white")
        self.board[7][5] = Bishop("WhiteBishopRight", (7, 5), "white")
        self.board[7][6] = Knight("WhiteKnightRight", (7, 6), "white")
        self.board[7][7] = Rook("WhiteRookRight", (7, 7), "white")

        self.board[2][6] = Knight("TestKnight", (2, 6), "white")
        self.board[5][6] = Knight("TestKnight2", (5, 6), "black")

        self.selected_piece = None

    def draw(self, win):
        '''
        Draws everything on the board(pieces, available moves)
        '''

        # draw pieces on the board
        for i in range(8):
            for j in range(8):
                if self.board[i][j] != 0:
                    self.board[i][j].draw(win)

        # draw available moves of the selected piece
        if self.selected_piece:
            self.selected_piece.draw_moves(win, self.board)

    def select(self, col, row):
        '''
        Select a piece on the board with coordinates (col, row).w
        '''
        for i in range(8):
            for j in range(8):
                if self.board[i][j] != 0:
                    self.board[i][j].selected = False

        # Check if (col, row) is piece
        if isinstance(self.board[row][col], Piece):
            self.board[row][col].selected = True
            self.selected_piece = self.board[row][col]
        else:
            self.selected_piece = None

        print(self.selected_piece)
