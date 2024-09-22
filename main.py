import pygame as pg
from random import random
from random import randrange
from colors import *
from game_of_life import *
import sys

def get_rect(x, y):
    return x * TILE + 1, y * TILE + 1, TILE - 2, TILE - 2


cols, rows = 30, 20
TILE = 30
WIN_WIDTH = cols * TILE
WIN_HEIGHT = rows * TILE
RES = WIN_WIDTH, WIN_HEIGHT

def run_logic(screen):
    cells = [[0 for _ in range(cols)] for _ in range(20)]
    glider = [[0, 0, 1, 0, 0],
              [0, 0, 0, 1, 0],
              [0, 1, 1, 1, 0]]

    for i, f in enumerate(glider):
        for j, b in enumerate(glider[i]):
            cells[i][j] = glider[i][j]

    while True:
        screen.fill(pg.Color('black'))
        [[pg.draw.rect(screen, pg.Color(colors[randrange(0,4)]), get_rect(x, y), border_radius=TILE // 10)
          for x, col in enumerate(row) if col] for y, row in enumerate(cells)]
        # draw_grid(screen=screen, win_width=WIN_WIDTH, win_height=WIN_HEIGHT, color='grey', cellsize=TILE)

        cells = get_next_generation(cells)

        pg.time.delay(500)
        pg.display.flip()
        [exit() for event in pg.event.get() if event.type == pg.QUIT]


if __name__ == '__main__':
    pg.init()
    screen = pg.display.set_mode([cols * TILE, rows * TILE])
    run_logic(screen)
