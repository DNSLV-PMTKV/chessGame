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


def connect():
    return n.board


def menu_screen():
    run = True
    while run:
        win.fill((128, 128, 128))
        font = pygame.font.SysFont("Ubuntu", 80)
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
    main()


def redraw_gameWindow():
    win.fill((128, 128, 128))
    win.blit(BOARD, (0, 0))
    board.draw(win)
    font = pygame.font.SysFont("comicsans", 30)
    txt = font.render("Press q to Quit", 1, (255, 255, 255))
    win.blit(txt, (800, 765))

    if board.turn == 'white':
        txt3 = font.render("ON TURN: WHITE", 1, (0, 0, 0))
        win.blit(txt3, (800, 400))
    else:
        txt3 = font.render("ON TURN: BLACK", 1, (0, 0, 0))
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
    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(5)
        redraw_gameWindow()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos_on_click = pygame.mouse.get_pos()
                i, j = click(mouse_pos_on_click)
                board.click(i, j)

    # menu_screen(win)


if __name__ == "__main__":
    menu_screen()
