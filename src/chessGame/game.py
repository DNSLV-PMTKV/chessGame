import pygame
import os
from board import Board
from client import Network

absFilePath = os.path.abspath(__file__)
fileDir = os.path.dirname(os.path.abspath(__file__))
parentDir = os.path.dirname(fileDir)

ROOT_DIR = os.path.dirname(parentDir)
IMG_DIR = os.path.join(ROOT_DIR, 'img')

board_img = os.path.join(IMG_DIR, 'board.png')
icon_img = os.path.join(IMG_DIR, 'chess_icon.ico')

BOARD = pygame.transform.scale(
    pygame.image.load(board_img), (800, 800))
WIDTH = 1000
HEIGHT = 800
win = pygame.display.set_mode((WIDTH, HEIGHT))
icon = pygame.image.load(icon_img)
pygame.display.set_icon(icon)
pygame.display.set_caption("Chess Game")

board = Board()
pygame.font.init()


def menu_screen():
    run = True
    while run:
        win.fill((128, 128, 128))
        font = pygame.font.SysFont("comicsans", 80)
        title = font.render("Chess Game!", 1, (0, 200, 0))
        join = font.render("Click To Join a Game!", 1, (0, 128, 0))
        font2 = pygame.font.SysFont("comicsans", 20)
        made_by = font2.render("Made by DNSLV-PMTKV", 1, (0, 0, 0))
        win.blit(title, (WIDTH / 2 - title.get_width() / 2, 200))
        win.blit(join, (WIDTH / 2 - join.get_width() / 2, 400))
        win.blit(made_by, (825, 775))
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                run = False
    while True:
        try:
            global board, n
            n = Network()
            board = n.board
            break
        except:
            print("Server offline")

    main()


def end_screen(text):
    pygame.font.init()
    font = pygame.font.SysFont("comicsans", 80)
    txt = font.render(text, 1, (255, 0, 0))
    win.blit(txt, (WIDTH / 2 - txt.get_width() / 2, 300))
    pygame.display.update()

    pygame.time.set_timer(pygame.USEREVENT + 1, 3000)

    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                run = False
            elif event.type == pygame.KEYDOWN:
                run = False
            elif event.type == pygame.USEREVENT + 1:
                run = False

    # menu_screen()


def redraw_gameWindow(board, color):
    win.fill((128, 128, 128))
    win.blit(BOARD, (0, 0))
    board.draw(win)
    font = pygame.font.SysFont("comicsans", 30)
    txt = font.render("Press q to Quit", 1, (255, 255, 255))
    win.blit(txt, (800, 765))

    if not board.players:
        font = pygame.font.SysFont("comicsans", 80)
        txt = font.render("Waiting for Player", 1, (255, 0, 0))
        win.blit(txt, (400 - txt.get_width() / 2, 350))

    font = pygame.font.SysFont("comicsans", 30)
    if color == "white":
        txt3 = font.render("YOU ARE WHITE", 1, (0, 0, 0))
        win.blit(txt3, (800, 100))
    else:
        txt3 = font.render("YOU ARE BLACK", 1, (0, 0, 0))
        win.blit(txt3, (800, 100))

    if board.turn == color:
        txt3 = font.render("YOUR TURN", 1, (0, 0, 0))
        win.blit(txt3, (800, 400))
    else:
        txt3 = font.render("THEIR TURN", 1, (0, 0, 0))
        win.blit(txt3, (800, 400))

    pygame.display.update()


def click(pos):
    """
    Returns position between (0-7),(0,7)
    """
    x = int(pos[0] / 100)
    y = int(pos[1] / 100)
    return (x, y)


def main():
    global board, n
    color = board.start_user
    clock = pygame.time.Clock()
    print(color)
    print(board.players)
    count = 0
    run = True

    while run:
        clock.tick(5)
        if count == 5:
            board = n.send("get")
            count = 0
        else:
            count += 1
        redraw_gameWindow(board, color)

        if board.check_mate("white"):
            board = n.send("winner b")
        elif board.check_mate("black"):
            board = n.send("winner w")

        if board.winner == "white":
            end_screen("White is the Winner!")
            run = False
        elif board.winner == "black":
            end_screen("Black is the winner")
            run = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    if color == "white":
                        board = n.send("winner b")
                    else:
                        board = n.send("winner w")
            if event.type == pygame.MOUSEBUTTONUP:
                if color == board.turn and board.players:
                    mouse_pos_on_click = pygame.mouse.get_pos()
                    i, j = click(mouse_pos_on_click)
                    board = n.send("select {} {}".format(i, j))

    n.disconnect()
    board = 0
    menu_screen()


if __name__ == "__main__":
    menu_screen()
