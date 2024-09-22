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

class Game:
    def __init__(self):
        self.cells = None
        pg.init()
        #pg.mouse.set_visible(False)
        self.screen = pg.display.set_mode(RES)
        pg.display.set_caption("Game Of Life")
        self.new_game()

    '''all game objects inizialization'''
    def new_game(self):
        self.cells = [[0 for _ in range(cols)] for _ in range(rows)]
        self.init_glider()

    def draw_grid(self, color='black', cellsize=20, add_numbers=False):
        font = pg.font.SysFont('arial', 20)
        for x in range(0, self.screen.get_width(), cellsize):
            pg.draw.line(self.screen, color, (x, 0), (x, self.screen.get_height()))
            if add_numbers:
                num_x = font.render(f'{x}', True, color)
                self.screen.blit(num_x, (x + 2, 0))
        for y in range(0, self.screen.get_height(), cellsize):
            pg.draw.line(self.screen, color, (0, y), (self.screen.get_width(), y))
            if add_numbers:
                num = font.render(f'{y}', True, color)
                self.screen.blit(num, (0, y + 2))
    def init_glider(self):
        glider = [[0, 0, 1, 0, 0],
                  [0, 0, 0, 1, 0],
                  [0, 1, 1, 1, 0]]

        for i, f in enumerate(glider):
            for j, b in enumerate(glider[i]):
                self.cells[i][j] = glider[i][j]

    def update(self):
        pg.display.flip()

    def run_logic(self):
        self.cells = get_next_generation(self.cells)
        pg.time.delay(500)



    def draw(self):
        self.screen.fill(pg.Color('black'))
        [[pg.draw.rect(self.screen, pg.Color(colors[randrange(0, 4)]), get_rect(x, y), border_radius=TILE // 10)
          for x, col in enumerate(row) if col] for y, row in enumerate(self.cells)]
        self.draw_grid(color='darkgrey', cellsize=30)
        pg.display.flip()

    def check_events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT or (event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE):
                pg.quit()
                sys.exit()

    '''combine all Game's calls in one method and run continiosly '''
    def run(self):
        while True:
            self.check_events()
            self.run_logic()
            self.draw()
            self.update()

if __name__ == '__main__':
    game = Game()
    game.run()
#



