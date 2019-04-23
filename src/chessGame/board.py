from pieces import *


class Board:
    def __init__(self):
        # initialize board as 2d array of 0's
        self.board = [[0 for x in range(8)] for y in range(8)]

        # black pawns
        for i in range(8):
            self.board[1][i] = Pawn(
                "BlackPawn{}".format(i + 1), (1, i), "black")

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
            self.board[6][i] = Pawn(
                "WhitePawn{}".format(i + 1), (6, i), "white")

        # white pieces
        self.board[7][0] = Rook("WhiteRookLeft", (7, 0), "white")
        self.board[7][1] = Knight("WhiteKnightLeft", (7, 1), "white")
        self.board[7][2] = Bishop("WhiteBishopLeft", (7, 2), "white")
        self.board[7][3] = Queen("WhiteQueen", (7, 3), "white")
        self.board[7][4] = King("WhiteKing", (7, 4), "white")
        self.board[7][5] = Bishop("WhiteBishopRight", (7, 5), "white")
        self.board[7][6] = Knight("WhiteKnightRight", (7, 6), "white")
        self.board[7][7] = Rook("WhiteRookRight", (7, 7), "white")

        self.selected_piece = None

        self.turn = 'white'

        self.players = False

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

    def select(self, col, row, color):
        '''
        Select a piece on the board with coordinates (col, row)
        '''
        if self.board[row][col] != 0 and self.board[row][col].color == color:
            self.selected_piece = self.board[row][col]
            print(self.selected_piece)
            print(self.selected_piece.available_moves(self.board))
            # self.board[row][col].selected = True
        else:
            self.selected_piece = None

    def click(self, col, row):
        if col < 8 and row < 8:
            if not self.selected_piece:
                self.select(col, row, self.turn)
            else:
                if (col, row) not in self.selected_piece.available_moves(self.board):
                    self.selected_piece = None
                else:
                    self.move((row, col))

    def move(self, pos):
        '''
        Move the selected piece from its position to another.
        '''
        test_board = self.board[:]
        old = self.selected_piece.position

        if isinstance(test_board[old[0]][old[1]], Pawn):
            test_board[old[0]][old[1]].first_move = False

        test_board[old[0]][old[1]].change_position(pos)
        test_board[pos[0]][pos[1]] = test_board[old[0]][old[1]]
        test_board[old[0]][old[1]] = 0

        self.board = test_board
        self.selected_piece = None

        if self.turn == 'white':
            self.turn = 'black'
        else:
            self.turn = 'white'

        if self.is_checked(self.turn):
            print("{} KING CHECKED !!!".format(self.turn.upper()))

    def danger(self, color):
        danger = []
        for i in range(8):
            for j in range(8):
                if self.board[i][j] != 0 and self.board[i][j].color != color:
                    for move in self.board[i][j].available_moves(self.board):
                        danger.append(move)
        return danger

    def is_checked(self, color):
        '''
        Return True if king is checked.
        '''
        for i in range(8):
            for j in range(8):
                if self.board[i][j] != 0 and self.board[i][j].color == color and isinstance(self.board[i][j], King):
                    king_pos = (j, i)

        if king_pos in self.danger(self.turn):
            return True
        return False
