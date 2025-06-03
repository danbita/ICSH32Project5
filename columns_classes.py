#gamestate.py


class Faller:
    def __init__(self, col: int, tiles: list[str]):
        self._col = col
        self._tiles = tiles

    def tiles(self) -> list[str]:
        'returns the tiles'
        return self._tiles

    def col(self) -> int:
        'returns the col the tiles repreenting the jewels are to be placed in'
        return self._col

class Board:
    def __init__(self, rows: int, cols: int, game_board: list[list[str]], status_board: list[list[str]]):
        self._rows = rows
        self._cols = cols
        self._game_board = game_board
        self._status_board = status_board
        self._landed = True
        for r in range(self._rows + 3):
            game_row = []
            status_row = []
            for c in range(self._cols):
                game_row.append(' ')
                status_row.append(' ')
            self._game_board.append(game_row)
            self._status_board.append(status_row)
        
    def rows(self) -> int:
        'returns rows of board'
        return self._rows

    def cols(self) -> int:
        'returns columns of board'
        return self._cols

    def landed(self) -> bool:
        'returns whether faller is currently landed'
        return self._landed

    def game_over(self) -> bool:
        'determines if the game is over'
        for c in range(self._cols):
            for r in range(0, 3):
                if self._game_board[r][c] != ' ':
                    return True
        return False

    def faller_locked(self) -> bool:
        'determines whether a faller is in a locked state'
        
        row = -1
        for c in range(self._cols):
            for r in range(self._rows+2, 2, -1):
                if self._status_board[r][c] == '|':
                    row = r
                    break
        if row != -1:
            return True
        return False

    def rotate_board(self) -> None:
        'rotate a faller'
        
        col = 0
        row = 0
        for c in range(self._cols):
            for r in range(self._rows+2, 2, -1):
                if self._status_board[r][c] == '[' or self._status_board[r][c] == '|':
                    row = r
                    col = c
                    break
                    
        temp = self._game_board[row][col]
        self._game_board[row][col] = self._game_board[row-1][col]
        self._game_board[row-1][col] = self._game_board[row-2][col]
        self._game_board[row-2][col] = temp

    def place_faller(self, faller: Faller) -> None:
        'places a faller'

        col = faller.col()
        self.print()
        if self._game_board[3][col] == ' ':
            self._game_board[1][col] = faller.tiles()[0]
            self._game_board[2][col] = faller.tiles()[1]
            self._game_board[3][col] = faller.tiles()[2]
            
            self._status_board[1][col] = '['
            self._status_board[2][col] = '['
            self._status_board[3][col] = '['
        else:
            self._game_board[0][col] = faller.tiles()[0]
            self._game_board[1][col] = faller.tiles()[1]
            self._game_board[2][col] = faller.tiles()[2]
            self._status_board[0][col] = '['
            self._status_board[1][col] = '['
            self._status_board[2][col] = '['
            
    
    def move_left(self) -> None:
        'moves a faller to the left'
        
        col = 0
        row = 0
        for c in range(self._cols):
            for r in range(self._rows+2, 2, -1):
                if self._status_board[r][c] == '[' or self._status_board[r][c] == '|':
                    row = r
                    col = c
                    break

        if col == 0:
            return
          
        if self._game_board[row][col-1] == ' ' and self._game_board[row-1][col-1] == ' ' and self._game_board[row-2][col-1] == ' ':
            self._game_board[row][col-1] = self._game_board[row][col]
            self._game_board[row-1][col-1] = self._game_board[row-1][col]
            self._game_board[row-2][col-1] = self._game_board[row-2][col]
            
            self._status_board[row][col-1] = '['
            self._status_board[row-1][col-1] = '['
            self._status_board[row-2][col-1] = '['

            self._game_board[row][col] = ' '
            self._game_board[row-1][col] = ' '
            self._game_board[row-2][col] = ' '
            
            self._status_board[row][col] = ' '
            self._status_board[row-1][col] = ' '
            self._status_board[row-2][col] = ' '

    def move_right(self) -> None:
        'moves a faller to the right'
        
        col = 0
        row = 0
        for c in range(self._cols):
            for r in range(self._rows+2, 2, -1):
                if self._status_board[r][c] == '[' or self._status_board[r][c] == '|':
                    row = r
                    col = c
                    break

        if col == self._cols-1:
            return
                    
        if self._game_board[row][col+1] == ' ' and self._game_board[row-1][col+1] == ' ' and self._game_board[row-2][col+1] == ' ':
            self._game_board[row][col+1] = self._game_board[row][col]
            self._game_board[row-1][col+1] = self._game_board[row-1][col]
            self._game_board[row-2][col+1] = self._game_board[row-2][col]
            
            self._status_board[row][col+1] = '['
            self._status_board[row-1][col+1] = '['
            self._status_board[row-2][col+1] = '['

            self._game_board[row][col] = ' '
            self._game_board[row-1][col] = ' '
            self._game_board[row-2][col] = ' '
            
            self._status_board[row][col] = ' '
            self._status_board[row-1][col] = ' '
            self._status_board[row-2][col] = ' '

    def tick(self) -> bool:
        'ticks time as the game goes on'
        col = 0
        row = 0
        for c in range(self._cols):
            for r in range(self._rows+2, 2, -1):
                if self._status_board[r][c] == '[':
                    row = r
                    col = c
                    break

        if row == self._rows + 2:
            self.has_landed()
            return
        elif self._game_board[row+1][col] != ' ':
            self.has_landed()
            return
        
        self._game_board[row+1][col] = self._game_board[row][col]
        self._game_board[row][col] = self._game_board[row-1][col]
        self._game_board[row-1][col] = self._game_board[row-2][col]
        self._game_board[row-2][col] = ' '

        self._status_board[row+1][col] = '['
        self._status_board[row][col] = '['
        self._status_board[row-1][col] = '['
        self._status_board[row-2][col] = ' '

        if row+1 == self._rows + 2:
            self.has_landed()
            return

        if self._game_board[row+2][col] != ' ':
            self.has_landed()
            return

    def has_landed(self) -> None:
        'determines whether a faller has fallen or not, and changes the status board accoadingly'
        
        col = 0
        row = 0
        self._landed =  True
        for c in range(self._cols):
            for r in range(self._rows+2, 2, -1):
                if self._status_board[r][c] == '[':
                    row = r
                    col = c
                    break

        self._status_board[row][col] = '|'
        self._status_board[row-1][col] = '|'
        self._status_board[row-2][col] = '|'
    
    def get_board(self) -> list[str]:
        'returns the game board'
        return self._game_board

    def get_status_board(self) -> list[str]:
        'returns the status board'
        return self._status_board

    def horizontal_matches(self) -> bool:
        'marks any horizontal matches'

        match_found = False
        for r in range(3, self._rows + 3):
            for c in range(self._cols - 2):
                if self._game_board[r][c] == self._game_board[r][c+1] and self._game_board[r][c+1] == \
                   self._game_board[r][c+2] and self._game_board[r][c] != ' ':
                    self._status_board[r][c] = '*'
                    self._status_board[r][c+1] = '*'
                    self._status_board[r][c+2] = '*'
                    match_found = True
                    for index in range(c+3, self._cols):
                        if self._game_board[r][index] == self._game_board[r][c]:
                            self._status_board[r][index] = '*'
                        else:
                            break
        return match_found

    def reset_status_board(self) -> None:
        'resets the status board to a clean state'
        
        for r in range(self._rows + 3):
            for c in range(self._cols):
                self._status_board[r][c] = ' '

    def reset_top(self) -> None:
        'resets the top of the game board before dropping a new faller'
        for r in range(3):
            for c in range(self._cols):
                self._game_board[r][c] = ' '

    
    def vertical_matches(self) -> bool:
        'marks any vertical matches'

        match_found = False
        for c in range(self._cols):
            for r in range(self._rows + 1):
                if self._game_board[r][c] == self._game_board[r+1][c] and self._game_board[r+1][c] == \
                   self._game_board[r+2][c] and self._game_board[r][c] != ' ':
                    self._status_board[r][c] = '*'
                    self._status_board[r+1][c] = '*'
                    self._status_board[r+2][c] = '*'
                    match_found = True
                    for index in range(r + 3, self._rows + 3):
                        if self._game_board[index][c] == self._game_board[r][c]:
                            self._status_board[index][c] = '*'
                        else:
                            break
        return match_found

    def diagonal_matches(self) -> bool:
        'marks any diagonal matches'

        match_found = False
        for r in range(3, self._rows+1):
            for c in range(self._cols-2):
                if self._game_board[r][c] == self._game_board[r+1][c+1] and self._game_board[r+1][c+1] == \
                self._game_board[r+2][c+2] and self._game_board[r][c] != ' ':
                    self._status_board[r][c] = '*'
                    self._status_board[r+1][c+1] = '*'
                    self._status_board[r+2][c+2] = '*'
                    match_found = True
                    index = 3
                    while(r + index <= self._rows and c + index <= self._cols - 3):
                        if self._game_board[r+index][c+index] == self._game_board[r][c]:
                            self._status_board[index][c] = '*'
                        else:
                            break

        for r in range(3, self._rows + 1):
            for c in range(self._cols-1, 1, -1):
                if self._game_board[r][c] == self._game_board[r+1][c-1] and self._game_board[r+1][c-1] == \
                   self._game_board[r+2][c-2] and self._game_board[r][c] != ' ':
                    self._status_board[r][c] = '*'
                    self._status_board[r+1][c-1] = '*'
                    self._status_board[r+2][c-2] = '*'
                    index = 3
                    match_found = True
                    while(r + index <= self._rows and c + index <= self._cols - 3):
                        if self._game_board[r+index][c-index] == self._game_board[r][c]:
                            self._status_board[index][c] = '*'
                        else:
                            break
        return match_found


    def remove_matches(self) -> None:
        'cleans up any matches after being deleted'
        for r in range(self._rows + 3):
            for c in range(self._cols):
                if self._status_board[r][c] == '*':
                    self._game_board[r][c] = ' '

    def contains_matches(self) -> bool:
        'determines whether there are any matches on the board at an instant'
        for r in range(self._rows + 3):
            for c in range(self._cols):
                if self._status_board[r][c] == '*':
                    return True
        return False


    def drop_pieces(self) -> None:
        'drops each jewel as low as possible'
        
        while not self.is_fallen():
            for c in range(len(self._game_board[0])):
                for r in range(len(self._game_board)-1, 2, -1):
                    if self._game_board[r][c] == ' ':
                        self._game_board[r][c] = self._game_board[r-1][c]
                        self._game_board[r-1][c] = ' '


    def is_fallen(self) -> bool:
        'determines whether a piece has fallen'

        for c in range(len(self._game_board[0])):
            last_found_tile = self._game_board[len(self._game_board)-1][c]
            for r in range(len(self._game_board)-2, 2, -1):
                if self._game_board[r][c] != ' ':
                    if last_found_tile == ' ':
                        return False
                last_found_tile = self._game_board[r][c]
        return True
                    
    def print(self) -> None:
        'prints the board (for this project this is for debugging purposes)'
        
        endline = ' '
        for r in range(0, self._rows + 3):
            line = '|'
            for c in range(self._cols):
                if self._status_board[r][c] == '[':
                    line += '[' + self._game_board[r][c] + ']'
                else:
                    line += self._status_board[r][c] + self._game_board[r][c] + self._status_board[r][c]
            line += '|'
            print(line, r)
        for c in range(self._cols):
            endline += '---'
        print(endline + ' ')


