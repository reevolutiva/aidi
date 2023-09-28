'''
This file contains the Game class which manages the game logic.
'''
class Game:
    def __init__(self):
        self.board_size = 15
        self.board = [[0] * self.board_size for _ in range(self.board_size)]
        self.current_player = 1
    def make_move(self, row, col):
        if self.board[row][col] == 0:
            self.board[row][col] = self.current_player
            self.current_player = 3 - self.current_player
    def check_winner(self):
        for i in range(self.board_size):
            for j in range(self.board_size):
                if self.board[i][j] != 0:
                    # Check horizontal
                    if j + 4 < self.board_size and self.board[i][j] == self.board[i][j+1] == self.board[i][j+2] == self.board[i][j+3] == self.board[i][j+4]:
                        return self.board[i][j]
                    # Check vertical
                    if i + 4 < self.board_size and self.board[i][j] == self.board[i+1][j] == self.board[i+2][j] == self.board[i+3][j] == self.board[i+4][j]:
                        return self.board[i][j]
                    # Check diagonal (top-left to bottom-right)
                    if i + 4 < self.board_size and j + 4 < self.board_size and self.board[i][j] == self.board[i+1][j+1] == self.board[i+2][j+2] == self.board[i+3][j+3] == self.board[i+4][j+4]:
                        return self.board[i][j]
                    # Check diagonal (top-right to bottom-left)
                    if i + 4 < self.board_size and j - 4 >= 0 and self.board[i][j] == self.board[i+1][j-1] == self.board[i+2][j-2] == self.board[i+3][j-3] == self.board[i+4][j-4]:
                        return self.board[i][j]
        return 0