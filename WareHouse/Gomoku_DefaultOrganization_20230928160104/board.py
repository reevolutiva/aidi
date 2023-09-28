'''
This file contains the Board class which handles the graphical representation of the game board.
'''
import tkinter as tk
class Board:
    def __init__(self, root, game):
        self.root = root
        self.game = game
        self.canvas = tk.Canvas(self.root, width=600, height=600, bg="white")
        self.canvas.pack()
    def draw_board(self):
        for i in range(self.game.board_size):
            self.canvas.create_line(50 + i * 40, 50, 50 + i * 40, 610, width=2)
            self.canvas.create_line(50, 50 + i * 40, 610, 50 + i * 40, width=2)
        self.canvas.bind("<Button-1>", self.player_handler.handle_click)  # Access the player handler instance using self.player_handler
    def draw_stone(self, row, col):
        x = 50 + col * 40
        y = 50 + row * 40
        if self.game.current_player == 1:
            self.canvas.create_oval(x - 15, y - 15, x + 15, y + 15, fill="black")
        else:
            self.canvas.create_oval(x - 15, y - 15, x + 15, y + 15, fill="white")
        winner = self.game.check_winner()
        if winner != 0:
            self.canvas.unbind("<Button-1>")
            if winner == 1:
                self.canvas.create_text(325, 325, text="Black wins!", font=("Arial", 24), fill="black")
            else:
                self.canvas.create_text(325, 325, text="White wins!", font=("Arial", 24), fill="black")