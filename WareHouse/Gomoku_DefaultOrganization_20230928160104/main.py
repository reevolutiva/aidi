'''
This is the main file of the Gomoku game. It initializes the game and starts the GUI.
'''
import tkinter as tk
from game import Game
from board import Board
from player import PlayerHandler
class GomokuGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Gomoku")
        self.game = Game()
        self.board = Board(self.root, self.game)
        self.player_handler = PlayerHandler(self.root, self.game, self.board)  # Pass the board instance to the player handler
        self.board.draw_board()
        self.root.mainloop()
if __name__ == "__main__":
    root = tk.Tk()
    gomoku_gui = GomokuGUI(root)