#project5.py

import pygame
import random
from columns_classes import *

colors = {
    ' ': pygame.Color('white'),
    'R': pygame.Color('red'),
    'O': pygame.Color('orange'),
    'Y': pygame.Color('yellow'),
    'G': pygame.Color('green'),
    'B': pygame.Color('blue'),
    'P': pygame.Color('purple'),
    'T': pygame.Color('tan')
}

class ColumnsGame():
    def __init__(self):
        self._running = True
        self._falling = False

        empty_row = []
        empty_list = []
        contents = [empty_row, empty_row, empty_row]
        status_board = [empty_list, empty_list, empty_list]
        
        self._board = Board(13, 6, [], [])


    def run(self) -> None:
        'runs the game'
        pygame.init()
        pygame.display.set_mode([300, 650], pygame.RESIZABLE)
        clock = pygame.time.Clock()

        while self._running:
            clock.tick(2)
            if not self._falling:
                self._board.reset_status_board()
                self._board.reset_top()
                self._create_new_faller()
                self._board.print()
                self._falling = True
            elif not self._handle_input():
                self._board.tick()

            check_end = False
            if self._board.faller_locked():
                if self._check_matches():
                    clock.tick(2)
                self._board.drop_pieces()
                self._board.tick()
                self._falling = False
                check_end = True
            #self._board.print()
            self._draw()
            if check_end:
                if self._board.game_over():
                    print('GAME OVER')
                    break

        pygame.quit()
    
        
    def _draw(self) -> None:
        'draws the board'
        surface = pygame.display.get_surface()
        surface.fill(pygame.Color(255, 255, 255))

        board = self._board.get_board()
        
        for r in range(3, 16):
            for c in range(6):
                rect = pygame.Rect(50 * c, 50 * (r-3), 50, 50)
                pygame.draw.rect(surface, colors[board[r][c]], rect)
                pygame.draw.rect(surface, pygame.Color('black'), rect, 1)
        
        pygame.display.flip()

    def _create_new_faller(self):
        'creates a new faller object to be placed into the board'
        col = random.randint(0, 5)
        jewels = ['R', 'O', 'Y', 'G', 'B', 'P', 'T']
        tiles = []
        tiles.append(jewels[random.randint(0, 6)])
        tiles.append(jewels[random.randint(0, 6)])
        tiles.append(jewels[random.randint(0, 6)])
        faller = Faller(col, tiles)
        self._board.place_faller(faller)
        

    def _handle_input(self) -> bool:
        '''
        handles game events, if a key with a role is pressed it returns
        true, otherwise it returns false
        '''
        
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    #move left
                    self._board.move_left()
                    return True
                elif event.key == pygame.K_RIGHT:
                    #move right
                    self._board.move_right()
                    return True
                elif event.key == pygame.K_SPACE:
                    #rotate
                    self._board.rotate_board()
                    return True
                elif event.key == pygame.K_q:
                    #quit
                    print('quit')
                    self._running = False
                    return True

        return False

    def _check_matches(self) -> bool:
        'checks for any matches'

        self._board.reset_status_board()
        if self._board.horizontal_matches() or self._board.vertical_matches() \
           or self._board.diagonal_matches():
            self._draw()
            self._board.remove_matches()
            self._board.print()
            self._board.tick()
            return True
        return False


if __name__ == '__main__':
    ColumnsGame().run()


'''
[
    ['O', ' ', ' ', ' ', ' ', ' '],
    ['O', ' ', ' ', ' ', ' ', ' '],
    ['O', ' ', ' ', ' ', ' ', ' '],
    ['G', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', ' ']
]'''
