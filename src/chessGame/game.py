import pygame
from board import Board
from client import Network

BOARD = pygame.transform.scale(
    pygame.image.load('../../img/board.png'), (800, 800))
WIDTH = 1000
HEIGHT = 800

win = pygame.display.set_mode((WIDTH, HEIGHT))
board = Board()
pygame.font.init()


# n = Network()
# n.print()


def menu_screen():
    run = True
    while run:
        win.fill((128, 128, 128))
        font = pygame.font.SysFont("comicsans", 80)
        title = font.render("Online Chess!", 1, (0, 200, 0))
        join = font.render("Click To Join a Game!", 1, (0, 128, 0))
        win.blit(title, (WIDTH/2 - title.get_width()/2, 200))
        win.blit(join, (WIDTH / 2 - join.get_width() / 2, 400))
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


def redraw_gameWindow(board, color):
    win.fill((128, 128, 128))
    win.blit(BOARD, (0, 0))
    board.draw(win)
    font = pygame.font.SysFont("comicsans", 30)
    txt = font.render("Press q to Quit", 1, (255, 255, 255))
    win.blit(txt, (800, 765))

    # if board.turn == 'white':
    #     txt3 = font.render("ON TURN: WHITE", 1, (0, 0, 0))
    #     win.blit(txt3, (800, 400))
    # else:
    #     txt3 = font.render("ON TURN: BLACK", 1, (0, 0, 0))
    #     win.blit(txt3, (800, 400))
    if not board.players:
        font = pygame.font.SysFont("comicsans", 80)
        txt = font.render("Waiting for Player", 1, (255, 0, 0))
        win.blit(txt, (WIDTH/2 - txt.get_width()/2, 300))

    font = pygame.font.SysFont("comicsans", 30)
    if color == "white":
        txt3 = font.render("YOU ARE WHITE", 1, (255, 0, 0))
        win.blit(txt3, (WIDTH / 2 - txt3.get_width() / 2, 10))
    else:
        txt3 = font.render("YOU ARE BLACK", 1, (255, 0, 0))
        win.blit(txt3, (WIDTH / 2 - txt3.get_width() / 2, 10))

    if board.turn == color:
        txt3 = font.render("YOUR TURN", 1, (255, 0, 0))
        win.blit(txt3, (WIDTH / 2 - txt3.get_width() / 2, 700))
    else:
        txt3 = font.render("THEIR TURN", 1, (255, 0, 0))
        win.blit(txt3, (WIDTH / 2 - txt3.get_width() / 2, 700))

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
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                run = False
            if event.type == pygame.MOUSEBUTTONUP:
                if color == board.turn and board.players:
                    mouse_pos_on_click = pygame.mouse.get_pos()
                    i, j = click(mouse_pos_on_click)
                    board = n.send("select {} {}".format(i, j))

    # menu_screen(win)


if __name__ == "__main__":
    menu_screen()
