'''
This file contains the PlayerHandler class which handles the player's moves.
'''
import tkinter as tk
class PlayerHandler:
    def __init__(self, root, game, board):
        self.root = root
        self.game = game
        self.board = board  # Store the board instance
        self.canvas = tk.Canvas(self.root, width=600, height=600, bg="white")
        self.canvas.pack()
    def handle_click(self, event):
        row = (event.y - 50) // 40
        col = (event.x - 50) // 40
        self.game.make_move(row, col)
        self.board.draw_stone(row, col)  # Access the board instance using self.board