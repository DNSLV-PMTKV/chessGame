import pygame
from board import Board

BOARD = pygame.transform.scale(
    pygame.image.load('../../img/board.png'), (800, 800))
WIDTH = 800
HEIGHT = 800

win = pygame.display.set_mode((WIDTH, HEIGHT))
board = Board()


def redraw_gameWindow():
    win.blit(BOARD, (0, 0))
    board.draw(win)

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
                board.select(i, j)


if __name__ == "__main__":
    main()
